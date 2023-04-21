#mqtt

En este repositorio se encuentran los 6 ejercicios pedidos en la tarea de mqtt del campus virtual: 

1.- 01_broker.py es un borker para realizar pruebas y ver que todos los ejercicios siguientes estaban funcionando correctamente mandando los mensajes
deseados a los topic elejidos.

2.- 02_numers.py se trata de un cliente que lee el topic numbers y realiza dos tareas: La primera tarea que he realizado es que compruebe que 
es entero o real y una vez hecho esto lo publique en numbers/real o numbers/entero y la segunda tarea consiste en ver si es primo o no y 
en caso de serlo se publicará en numbers/prime

3.- 03_temperature.py es un cliente que lee los subtopics de temperature/ y pasados  10 segundos calcula las temperaturas máximas, medias y minimas
de cada subtopic por separado y de todos juntos.

4.- 04_humidity.py es un cliente que cuando la temperatura sobrepasa de una constante K_0 (en este caso 15) empieza a escuchar el topic de la humedad.
En caso de que la temperatura baje de K_0 o que la humedad baje de otra constante K_1 (en nuestro caso 75) deja de escuchar el toopic de humedad y 
volvemos al principio, solo escuchar temperature hasta superar K_0 ...

5.- 05_temporizador.py es un cliente que recibe un mensaje en el siguiente formato: [tiempo de espera],[topic],[mensaje] y es el encargado de esperar
el tiempo dado y mandar el mensaje en el topic pedido.

6.- 06_clientes_encadenados.py para este cliente he decidido que si el numero recibido en clients/pablo es primo se imprime por pantalla la tamperatura
leida del topic temperature/t1 esperando sleep(10). Una vez pasado este tiempo en el canal aparece b'stop' y se desuscribe del canal temperature/t1. 
