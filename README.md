# snet-centivize
Docker and DigitalOcean Droplet server code for uploading Centivize's summarization and similarity ML algorithms to SingularityNET for public use.

**Usage - Command Line**
*Similarity Service*
`snet client call centivize-org centivize default_group similarity '{"par1":"[INSERT PARAGRAPH 1 HERE]","par2":"[INSERT PARAGRAPH 2 HERE]"}' -y`
*Summarization Service*
1. `nano /tmp/my_paragraph.txt`
2. Insert your long paragraph, then save and close the file (`^O, ^X`). 
3. `snet client call centivize-org centivize default_group summarize '{"file@par": "/tmp/my_paragraph.txt", "num": [YOUR NUMBER HERE, recommended number is 11]}' -y`
