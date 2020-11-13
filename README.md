## Run in Docker

1. Clone repo with all submodules `git clone git@github.com:wiating-app/wiating_devops.git --recursive`
2. Copy `.env.example` file to `.env` and replace `XXXXX` inside with a correct secrets.
3. Execute `docker-compose up`
4. To initialize database execute `docker-compose exec app bash ./scripts/initialize_database.sh`

## Run in Vagrant

1. Create `admin` user, add to `sudo` group
1. Put all your secrets into `/opt/.env` file
1. Put S3 secrets into `/home/admin/.aws/credentials` (according to boto3)
1. Put Flask dashboard config into `/opt/dashboard.cfg` file
1. Run ansible
