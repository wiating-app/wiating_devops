## Run in docker

1. Clone repo with all submodules
1. If needed edit `.env` file
1. Execute `docker-compose up`
1. To initialize database execute `docker-compose exec app bash ./scripts/initialize_database.sh`

## Run in Vagrant

1. Create `admin` user, add to `sudo` group
1. Put all your secrets into `/opt/.env` file
1. Put S3 secrets into `/home/admin/.aws/credentials` (according to boto3)
1. Put Flask dashboard config into `/opt/dashboard.cfg` file
1. Run ansible
