from split_settings.tools import optional, include

include(
    # Load environment settings
    'base/env.py',
    optional('local/env.py'),  # We can "patch" any settings from local folder env.py file.

    # Here we should have the order because of dependencies
    'base/jet.py',
    'base/paths.py',
    'base/apps.py',
    'base/middleware.py',
    'base/storages.py',

    # Load all other settings
    'base/*.py',

    optional('local/*.py'),  # we can load any other settings from local folder
)
