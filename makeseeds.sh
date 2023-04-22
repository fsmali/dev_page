python3 manage.py dumpdata skills --output skills/seeds.json --indent=2;
python3 manage.py dumpdata projects --output projects/seeds.json --indent=2;
python3 manage.py dumpdata developers --output developers/seeds.json --indent=2;
python3 manage.py dumpdata comments --output comments/seeds.json --indent=2;
python3 manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;
