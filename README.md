# Digital Dryroom

## Where to find the data

1. Kadi4Mat: https://kadi4mat.iam.kit.edu/collections/5921
2. Time Series Database: Currently located on **sxv20590.ise.fhg.de** (see below how to connect).

## Architecture

> Arrows Indicate direction of who is initializing the communication !!!

Orange components are hosted on the **wm20549**. 
Blue components are hosted on ISE servers. 

(Yes, the communication 
goes back and forth between the dryroom and the ISE servers - yet we believe thats okay for now.)

<img src="docs/architecture.drawio.png" alt="isolated" width="600"/>

## How to Start Production

1. Login into **wm20549** as "messcelllab" (password ask kapil, tobi or alex)
2. Start Node-RED
    1. Start the service by running `node-red` in powershell
    2. Visit the admin interface by using the link on the desktop
3. Connect to TimescaleDB
   1. Run `psql -h sxv20590.ise.fhg.de -U batt_admin -d tsdb` (passowrd see `config.py`)
   2. List all tables `\dt`
   3. Get latest data from one table:
      ```
      SELECT *
      FROM efm_filling_static
      ORDER BY timestamp DESC
      LIMIT 20;
      ```
4. Connect to RabbitMQ
   1. Visit https://hub.ise.fraunhofer.de/ in the browser
   2. Login as "dryroom-admin" (passowrd see `config.py`)
   3. Go to Queues / opcua_data to check incoming data from node-red
5. Start Python Data Preprocessing Service by starting `start_data_processing_service.bat` located on the desktop.
6. Start Rest API 
   1. visit `http://127.0.0.1:8000/docs` for API documentation

## How To Add New Machine

### Create Configuration on Node-Red
1. Login/Start Node-RED see above
2. Create new "Tab" which contains all information about one machine or part of a machine. Each Tab in Node-RED 
   corresponds to two DB tables (1) static data, and (2) time series data
3. Configure new machine according to the other Tabs :)

### Create RabbitMQ Queue

Data from Node-Red is written into RabbitMQ, where it is pulled from the Python preprocessing service. The following
steps describe how to set up a new Queue:
1. Log into RabbitMQ and switch to Queues
2. Add Queue
3. Configure binding for the queue: Exchange is `digital_dryroom`, Routing key is configured in Node-RED 
4. Test the configuration by triggering injections from Node-RED and see if Ready/Total messages increase in RabbitMQ

### Create Schema

Create new Schema which matches the configuration in Node-RED
1. Schemas are stored in Python at: `digital_dryroom/schema`
2. Create new file for the new machine according to the old schemas
3. Make sure to add schema to `all_schemas` in `schema/__init__.py`
4. Don´t forget to commit, push and merge into main.

### Create Table in DB

1. Use script `database_init/create_db.py` to either create the new table (or all tables according to the scheme definition)

### Add new Scheme to the preprocessing Pipeline

1. Add new `Channel` to `channels` in `data_preprocessing/main.py`. Take care that the name must match the name of the 
   RabbitMQ queue.
2. Restart the preprocessing service and check the console output/log for fields which don't match the schema.

### Troubleshooting

1. **Sometimes old potential faulty messages are stored in the queue which cannot be consumed by the preprocessing 
   service:** To fix this, log into RabbitMQ / go to Queues /  `Purge Messages` of the queue in doubt. Ready Messages
   of that queue should be 0 now. Now, try to restart the preprocessing service.

## How To Start Digital Twin

There is the option to run a "digital twin" of the productive environment on your local machine using
Docker. You can use this for development purposes without effecting the production environment.

> **Disclaimer:** Docker usage is restricted on ISE devices.
> It should only be used for creating the Dockerfile.

>  **Note:** It is recommended to use the **productive NodeRED and RabbitMQ environment** as data source, 
> as creating dummy data which mirrors the production setup is very cumbersome. Yet using them locally as a playground
> is also possible. But you have to configure NodeRED so it generates the data as it is expected by the preprocessing
> service.

1. `docker-compose up` in the projects root directory. 
2. Check if `PROD_DATABSE=False` in `config.py`
3. Start like described above
4. Database: Connect via `docker exec -it timescaledb psql -U user -d mydatabase`

> If you still want to use a local NodeRED and RabbitMQ, access it after starting docker-compose by:
1. NodeRED: http://localhost:1880/
   1. Import `dev_node_red_config.json`
2. RabbitMQ: http://localhost:15672/ (passowrd see `config.py`)
3. Check if `PROD_RABBITMQ=False` in `config.py`

For a clean shutdown: `docker-compose down -v`

## How to Setup and Configure
<div id="setup"></div>

> **Disclaimer:** 
> 1. Make sure to use a **virtual python environment** before installing the
> dependencies defined in the requirements.txt files !!!!1!! Conda is recommended.
> 2. These steps were done on the production server **wm20549** already, so no need to do it there.

1. Node-Red
    1. Install `@meowwolf/node-red-contrib-amqp` and `node-red-contrib-postgresql`
    2. Import the configuration stored at `node_red/node_red_config.json`
    3. Update user and password in the rabbitMQ config
2. RabbitMQ: Create a Queue and bind the exchange `bfm_data`
3. TimescaleDB configuration:
   1. install `requirements.txt`
   2. run `create_db.py`, if it fails, first drop the tables
4. Data Preprocessing
   1. install `requirements.txt`
