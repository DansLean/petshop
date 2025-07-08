from flask import Flask, request, jsonify

lista = [{"id": 1, "name": "Peter", "age": 22}, ]
id_count = 1

# mostra todos os elementos da lista
# mostra um elemento da lista por id
# adiciona um treco na lista
# edita um treco na lista por id
# deleta um treco na lista por id

app = Flask(__name__)

@app.get("/lista/all")
def devolte_tudinho():
    return {"lista": lista}

@app.get("/lista/get/<int:busca_id>")
def busca_um_poquinho(busca_id: int):
    for i in lista:
        if i["id"] == busca_id:
            return i
    
    return {"error": "ihhhhh se deu mal heinnn :P"}

@app.post("/lista/add")
def mais_um_por_favor():
    data = request.get_json()

    if not data.get("name") or not data.get("age"):
        return {"error": "não seja ganancioso"}
    global id_count
    id_count += 1
    item_lista = {
        "id": id_count,
        "name": data.get("name"),
        "age": data.get("age")
    }

    lista.append(item_lista)
    return jsonify({"msg": "o bom filho a casa torna (transforma viu senhor guilherme)", "item_lista": item_lista}), 200
    # return {"msg": "", item_lista}

@app.put("/lista/edit/<int:edit_id>")
def edita_negocinho(edit_id: int):
    editar_item = None

    for i in lista:
        if i["id"] == edit_id:
            editar_item = i
    
    if editar_item is None:
        return {"error": "Congratulações! A loteria de outubro foi concluída"}
    
    data = request.get_json()

    editar_item["name"] = data.get("name")
    editar_item["age"] = data.get("age")

    lista[edit_id - 1] = editar_item
    return {"msg": "deu."}

@app.delete("/lista/delete/<int:delete_id>")
def tacos(delete_id: int):
    index_to_delete = -1
    for k, v in enumerate(lista):
        if int(v["id"]) == delete_id:
            index_to_delete = k
    
    if index_to_delete != -1:
        lista.pop(index_to_delete)
        return {"msg": "A Terça do Taco é hoje!!! (mesmo sendo uma sexta-feira)"}
    
    return {"error": "você não é um Mestre Construtor >:("}
