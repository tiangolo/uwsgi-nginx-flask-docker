#! /usr/bin/env sh

echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"

echo "
#! /usr/bin/env sh

# Let the DB start
sleep 10;
# Run migrations
alembic upgrade head
"
