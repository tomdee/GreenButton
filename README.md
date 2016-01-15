# InfluxDB for GreenButton data
This simple script converts Green Button data from pge.com into InfluxDB line format.

## Example usage
After downloading the CSV zip file of your usage from the pge.com website
`unzip -p data.zip |python convert2influxdb.py`> readings

## Inserting into InfluxDB
`curl -sS -i -XPOST "http://influxdb:8086/write?db=tomdee" --data-binary @readings`

## Building (Optional)
Create a binary with `pyinstaller -F convert2influxdb.py`


