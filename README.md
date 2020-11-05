# snet-centivize
Docker and DigitalOcean Droplet server code for uploading Centivize's summarization and similarity ML algorithms to SingularityNET for public use.

**Usage - Command Line (SingularityNET CLI)**

*Similarity Service*

`snet client call centivize-org centivize default_group similarity '{"par1":"[INSERT PARAGRAPH 1 HERE]","par2":"[INSERT PARAGRAPH 2 HERE]"}' -y`

*Summarization Service*
1. `nano /tmp/my_paragraph.txt`
2. Insert your long paragraph, then save and close the file (`^O, ^X`). 
3. `snet client call centivize-org centivize default_group summarize '{"file@par": "/tmp/my_paragraph.txt", "num": [YOUR NUMBER HERE, recommended number is 11]}' -y`

**Configuration (DigitalOcean Droplet)**

    ssh root@<droplet-ip>
    
    ORGANIZATION_ID="centivize"-org
    ORGANIZATION_NAME="Centivize"
    SERVICE_ID=centivize
    SERVICE_NAME="Centivize"
    SERVICE_IP=<droplet-ip>
    SERVICE_PORT=5001
    DAEMON_PORT=5000
    DAEMON_HOST=0.0.0.0
    USER_ID=$USER
    SNET_CLI_HOST=$HOME/.snet/
    SNET_CLI_CONTAINER=/root/.snet/
    ETCD_HOST=$HOME/.snet/etcd/example-service/
    ETCD_CONTAINER=/opt/singnet/etcd/

    docker run \
        --name CENTIVIZE \
        -e ORGANIZATION_ID=$ORGANIZATION_ID \
        -e ORGANIZATION_NAME="$ORGANIZATION_NAME" \
        -e SERVICE_ID=$SERVICE_ID \
        -e SERVICE_NAME="$SERVICE_NAME" \
        -e SERVICE_IP=$SERVICE_IP \
        -e SERVICE_PORT=$SERVICE_PORT \
        -e DAEMON_HOST=$DAEMON_HOST \
        -e DAEMON_PORT=$DAEMON_PORT \
        -e USER_ID=$USER_ID \
        -p $DAEMON_PORT-$DAEMON_PORT \
        -v $SNET_CLI_HOST:$SNET_CLI_CONTAINER \
        -v $ETCD_HOST:$ETCD_CONTAINER \
        -ti snet_publish_service bash
    
    git clone https://github.com/rvignav/snet-centivize.git
    cd snet-centivize
    pip install torch torchvision nltk transformers
    pip install -U sentence-transformers==0.3.4
    cd centivize-service
    sh buildproto.sh
    python3 run_centivize_service.py --daemon-config snetd.config.json
