punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

punto = (3, 4)  #parentesi tonde
print(punto[0]) # Output: 3
print(punto[1]) # Output: 4

punto = 3, 4   # Tuple packing
x, y = punto   # Tuple unpacking
print(x, y)    
# Output: 3 4

set1 = set([1, 2, 3, 4, 5]) #dentro una lista (con parentesi quadre), viene castata in un set
set2 = {4, 5, 6, 7, 8}

set3 = {1, 2, 3, 3, 4, 4, 5}    #parentesi graffe
print(set3)   
# Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))                  
print(set1.intersection(set2))           
print(set1.difference(set2))     #presenti nell'insieme di partenza ma non nell'altro insieme        
print(set1.symmetric_difference(set2))   #presenti in uno ma non nell'altro
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
# Output: {4, 5}
# Output: {1, 2, 3}
# Output: {1, 2, 3, 6, 7, 8}

studente = {
"nome": "Alice",
"età": 20,
"sesso": "Femmina"
}

print(studente["nome"])   
# Output: "Alice"
print(studente["età"])    
# Output: 20.


studente["età"] = 21    #a differenze delle tuple è modificabile
print(studente)   
# Output: 
{'nome': 'Alice', 'età': 21,  'sesso':'Femmina'}

studente["città"] = "Roma"
print(studente)   
# Output: 
{'nome': 'Alice','età': 21,'sesso':'Femmina', 'città': 'Roma'}
#posso addirittura inserire nuovi campi dinamicamente

studente = {
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
 }
print(studente.keys()) # Output: dict_keys(['nome', 'età', 'sesso'])
print(studente.values()) # Output: dict_values(['Alice', 20, 'Femmina'])

for x,y,z in studente.values():
    print(x, y, z)
