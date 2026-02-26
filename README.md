# test_data-monitoring-system

## Αρχιτεκτονική 
συλλογή μετρήσεων απο αισθητήρες με MQTT ,  αποθήκευση σε TimescaleDB και ανάκτηση τους μεσω FastAPI 

Publishers(1-3) (αισθητήρες) → Mosquitto broker (διακινηση mqtt messages) → Subscriber (παραλήπτης , λαμβανει και καταγραφει messages στην database) → Database 
![Screenshot](pipeline.png)

## Τρέχον Στάδιο
ολοκληρωθηκε το `docker-compose.yml` 