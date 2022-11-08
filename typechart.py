# Pokemon Type Table
# Effectiveness values
vEffective = 1.5
Effective = 1.0
nEffective = 0.5
notEffective = 0.0

# Dictionary of each Type
pkmn_types = {
 "Normal": {
  "Normal": Effective,
  "Fire": Effective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": Effective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": Effective,
  "Ground": Effective,
  "Flying": Effective,
  "Psychic": Effective,
  "Bug": Effective,
  "Rock": nEffective,
  "Ghost": notEffective,
  "Dragon": Effective,
 },
 "Fire": {
  "Normal": Effective,
  "Fire": nEffective,
  "Water": nEffective,
  "Electric": Effective,
  "Grass": vEffective,
  "Ice": vEffective,
  "Fighting": Effective,
  "Poison": Effective,
  "Ground": Effective,
  "Flying": Effective,
  "Psychic": Effective,
  "Bug": vEffective,
  "Rock": nEffective,
  "Ghost": Effective,
  "Dragon": nEffective,
 },
 "Water": {
  "Normal": Effective,
  "Fire": vEffective,
  "Water": nEffective,
  "Electric": Effective,
  "Grass": nEffective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": Effective,
  "Ground": vEffective,
  "Flying": Effective,
  "Psychic": Effective,
  "Bug": Effective,
  "Rock": vEffective,
  "Ghost": Effective,
  "Dragon": nEffective,
 },
 "Electric": {
  "Normal": Effective,
  "Fire": Effective,
  "Water": vEffective,
  "Electric": nEffective,
  "Grass": nEffective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": Effective,
  "Ground": notEffective,
  "Flying": vEffective,
  "Psychic": Effective,
  "Bug": Effective,
  "Rock": Effective,
  "Ghost": Effective,
  "Dragon": nEffective,
 },
 "Grass": {
  "Normal": Effective,
  "Fire": nEffective,
  "Water": vEffective,
  "Electric": Effective,
  "Grass": nEffective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": nEffective,
  "Ground": vEffective,
  "Flying": nEffective,
  "Psychic": Effective,
  "Bug": nEffective,
  "Rock": vEffective,
  "Ghost": Effective,
  "Dragon": nEffective,
 },
 "Ice": {
  "Normal": Effective,
  "Fire": Effective,
  "Water": nEffective,
  "Electric": Effective,
  "Grass": vEffective,
  "Ice": nEffective,
  "Fighting": Effective,
  "Poison": Effective,
  "Ground": vEffective,
  "Flying": vEffective,
  "Psychic": Effective,
  "Bug": Effective,
  "Rock": Effective,
  "Ghost": Effective,
  "Dragon": vEffective,
 },
 "Fighting": {
  "Normal": vEffective,
  "Fire": Effective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": Effective,
  "Ice": vEffective,
  "Fighting": Effective,
  "Poison": nEffective,
  "Ground": Effective,
  "Flying": nEffective,
  "Psychic": nEffective,
  "Bug": nEffective,
  "Rock": vEffective,
  "Ghost": notEffective,
  "Dragon": Effective,
 },
 "Poison": {
  "Normal": Effective,
  "Fire": Effective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": vEffective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": nEffective,
  "Ground": nEffective,
  "Flying": Effective,
  "Psychic": Effective,
  "Bug": vEffective,
  "Rock": nEffective,
  "Ghost": nEffective,
  "Dragon": Effective,
 },
 "Ground": {
  "Normal": Effective,
  "Fire": vEffective,
  "Water": Effective,
  "Electric": vEffective,
  "Grass": nEffective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": vEffective,
  "Ground": Effective,
  "Flying": notEffective,
  "Psychic": Effective,
  "Bug": nEffective,
  "Rock": vEffective,
  "Ghost": Effective,
  "Dragon": Effective,
 },
 "Flying": {
  "Normal": Effective,
  "Fire": Effective,
  "Water": Effective,
  "Electric": nEffective,
  "Grass": vEffective,
  "Ice": Effective,
  "Fighting": vEffective,
  "Poison": Effective,
  "Ground": Effective,
  "Flying": Effective,
  "Psychic": Effective,
  "Bug": vEffective,
  "Rock": nEffective,
  "Ghost": Effective,
  "Dragon": Effective,
 },
 "Psychic": {
  "Normal": Effective,
  "Fire": Effective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": Effective,
  "Ice": Effective,
  "Fighting": vEffective,
  "Poison": vEffective,
  "Ground": Effective,
  "Flying": Effective,
  "Psychic": nEffective,
  "Bug": Effective,
  "Rock": Effective,
  "Ghost": vEffective,
  "Dragon": Effective,
 },
 "Bug": {
  "Normal": Effective,
  "Fire": nEffective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": vEffective,
  "Ice": Effective,
  "Fighting": nEffective,
  "Poison": vEffective,
  "Ground": Effective,
  "Flying": nEffective,
  "Psychic": vEffective,
  "Bug": Effective,
  "Rock": Effective,
  "Ghost": nEffective,
  "Dragon": Effective,
 },
 "Rock": {
  "Normal": Effective,
  "Fire": vEffective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": Effective,
  "Ice": vEffective,
  "Fighting": nEffective,
  "Poison": Effective,
  "Ground": nEffective,
  "Flying": vEffective,
  "Psychic": Effective,
  "Bug": vEffective,
  "Rock": Effective,
  "Ghost": Effective,
  "Dragon": Effective,
 },
 "Ghost": {
  "Normal": notEffective,
  "Fire": Effective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": Effective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": Effective,
  "Ground": Effective,
  "Flying": Effective,
  "Psychic": vEffective,
  "Bug": Effective,
  "Rock": Effective,
  "Ghost": vEffective,
  "Dragon": Effective,
 },
 "Dragon": {
  "Normal": Effective,
  "Fire": Effective,
  "Water": Effective,
  "Electric": Effective,
  "Grass": Effective,
  "Ice": Effective,
  "Fighting": Effective,
  "Poison": Effective,
  "Ground": Effective,
  "Flying": Effective,
  "Psychic": Effective,
  "Bug": Effective,
  "Rock": Effective,
  "Ghost": Effective,
  "Dragon": vEffective,
 }
}
