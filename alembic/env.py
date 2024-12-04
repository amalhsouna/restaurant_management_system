from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.database import Base  # Chemin vers la base SQLAlchemy
from app.models.users import User  # Importez tous les modèles définis
from app.models.order import Order  # Si vous avez d'autres modèl

# Configurer le fichier de configuration
config = context.config

# Configurer le logger
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Associer target_metadata à vos modèles
target_metadata = Base.metadata


def run_migrations_offline():
    """Exécute les migrations en mode offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Exécute les migrations en mode online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
