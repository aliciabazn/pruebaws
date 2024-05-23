#Asignación de variables a los elementos de la secuencia de la insulina
#python3.6
#coding: utf-8
#longuitud maxima de las lineas--> \ para mantener el cumplimiento de la guía
# de estilo Propuestas de Mejora de Python (PEP) 8. La guía de estilo PEP 8 
# recomienda un máximo de 79 caracteres por línea.

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

print(preproInsulin)

#Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin
print(insulin)
print(insulin)
print(insulin)
print(insulin)

print(len(insulin))

# Printing "the sequence of human insulin" to console using successive print()
# commands:
print(f"The sequence of human preproinsulin: {preproInsulin}")
#o print(preproInsulin)

# Printing to console using concatenated strings inside the print function 
#(one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

print(f'The sequence of human insulin, chain b: {bInsulin}')

print("La secuencia señal de la preproinsulina contiene: ",len(lsInsulin),"aminoácidos.")
print("Y contiene una molecula de proinsulina de: ",len(aInsulin + bInsulin + cInsulin), "aminoácidos.")

#calculating the molecular weight of insulin: 
#vamos a calcular el peso molecular aproximado de la insulina 
#sooooooo

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Count the number of each amino acids
# CUENTA CUANTAS VECES CUANTOS AA HAY EN INSULINA Y CUANTAS VECES SE REPITEN
# upper convierte la secuencia en mayusculas, para contar de manera uniforme
# .count numero de vece que aa aparece en la secuencia
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aaWeights.keys()})
print(aaCountInsulin)

# Multiply the count by the weights of each aa
molecularWeightInsulin = ({x: float(aaCountInsulin[x]*aaWeights[x]) for x in
aaWeights}.values())  
print(molecularWeightInsulin)
#sumamos el total
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

