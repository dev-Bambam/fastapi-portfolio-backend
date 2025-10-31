from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base


# Import the settings from the new config file
from .config import settings 

# 1. Create the ASYNCHRONOUS Engine
engine = create_async_engine(
    settings.DB_URL, 
    echo=False,
    # === CRITICAL ADDITIONS FOR PGBOUNCER / SUPABASE ===
    
    # 1. Recycle connections every 280 seconds (4m 40s) 
    #    to beat the common 5-minute server idle timeout.
    pool_recycle=280, 
    
    # 2. Add a quick test query on checkout to confirm the connection is alive.
    pool_pre_ping=True, 
    
    # Optional: Adjust pool size if you have many concurrent users
    pool_size=15, 
    max_overflow=5
)

# 2. Create the Asynchronous Session Local
AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()


# 3. Asynchronous Dependency for FastAPI (This was already correct)
async def get_db():
    """Dependency that provides an asynchronous database session."""
    db = AsyncSessionLocal()
    try:
        yield db
        await db.commit() 
    except Exception as e:
        await db.rollback() 
        raise e
    finally:
        await db.close()

# 4. CORRECTED: ASYNCHRONOUS Database Initialization
async def db_init():
    """Initializes the database by creating all tables asynchronously."""
    print("Attempting to initialize database...")
    try:
        # Use engine.begin() for connection handling
        async with engine.begin() as conn:
            # CRITICAL: Use conn.run_sync() to safely execute synchronous operations
            # like create_all() on an async connection.
            await conn.run_sync(Base.metadata.create_all)
        print("Database initialized successfully (or tables already exist).")
    except Exception as e:
        # We print the actual error if initialization fails
        print(f"Error initializing database: {e}")

# Export Base and engine for migrations/metadata (if needed)
# __all__ = ["engine", "AsyncSessionLocal", "Base", "get_db", "db_init"] # Uncomment if needed
