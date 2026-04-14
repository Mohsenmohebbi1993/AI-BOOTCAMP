# Make json file by pyrhon
def make_json_file():
    """ make default **users.json**   
        30 user with favorite movie
    
    """
    import json

    users = {
            "Ali Hasani": ["Memento", "Prestige", "Fight Club", "Titanic", "Avatar"],
            "Mohsen Mohseni": ["Batman", "Prestige", "Fight Club", "Se7en", "Matrix"],
            "Sahar Karimi": ["Pulp Fiction", "Interstellar", "Gladiator", "Avatar", "The Godfather"],
            "Mohamad Alavi": ["Matrix", "Titanic", "Prestige", "Avatar", "Se7en"],
            "Hamir Moradi": ["Shutter Island", "Prestige", "Titanic", "Memento", "Gladiator"],
            "Alireza Ahmadi": ["Matrix", "Batman", "Interstellar", "Pulp Fiction", "Se7en"],
            "Koroush Rostakohan": ["Gladiator", "Avatar", "Fight Club", "Interstellar", "Prestige"],
            "Ali Ebrahimi": ["The Departed", "Matrix", "Se7en", "Prestige", "Shutter Island"],
            "Roz Asgharpour": ["Fight Club", "Memento", "Interstellar", "Titanic", "Avatar"],
            "Ali Kazemi": ["Matrix", "Prestige", "The Godfather", "Titanic", "Shutter Island"],
            "Karim Hasani": ["Titanic", "Se7en", "Avatar", "Matrix", "Fight Club"],
            "Jahan Mohseni": ["Inception", "Gladiator", "Memento", "Shutter Island", "The Departed"],
            "Monbina Karimi": ["Prestige", "Se7en", "Matrix", "Interstellar", "Avatar"],
            "Gelare Alavi": ["Fight Club", "The Departed", "Shutter Island", "Prestige", "Memento"],
            "Negin Moradi": ["Batman", "Avatar", "Titanic", "Matrix", "Gladiator"],
            "Tahere Ahmadi": ["Se7en", "Prestige", "Matrix", "Titanic", "Fight Club"],
            "Farhad Mohebbi": ["Avatar", "Prestige", "Shutter Island", "Pulp Fiction", "Memento"],
            "Sara Ebrahimi": ["The Departed", "Titanic", "Fight Club", "Prestige", "Se7en"],
            "Sara Rahmani": ["Matrix", "Prestige", "Interstellar", "Gladiator", "Avatar"],
            "Sara Kazemi": ["Shutter Island", "Matrix", "Pulp Fiction", "Prestige", "Avatar"],
            "Ahmad Hasani": ["Fight Club", "Prestige", "Matrix", "Avatar", "Shutter Island"],
            "Mohsen Kazeni": ["Titanic", "Interstellar", "Fight Club", "Prestige", "Batman"],
            "Reza Kermani": ["Pulp Fiction", "Avatar", "Se7en", "Prestige", "Inception"],
            "Bahram Mohamadpour": ["Memento", "Matrix", "Shutter Island", "Titanic", "Gladiator"],
            "Amirreza Moradpour": ["Prestige", "Fight Club", "Pulp Fiction", "Avatar", "Matrix"],
            "Mobin Hasanzadeh": ["The Departed", "Titanic", "Matrix", "Prestige", "Avatar"],
            "Amirhoseyn Rostami": ["Avatar", "Matrix", "Gladiator", "Se7en", "Inception"],
            "Maryam Ebrahimi": ["Se7en", "Prestige", "Shutter Island", "Inception", "The Godfather"],
            "Fatemeh Rahmani": ["Fight Club", "Prestige", "Pulp Fiction", "Matrix", "Avatar"],
            "Mahdie Kazemi": ["Titanic", "Avatar", "Prestige", "Shutter Island", "Matrix"]}

    # your path
    PATH = r"C:\Mohsen Folder\Ai Bootcamp\Ai Bootcamp\notebooks\Project\2. HW_L02_02_python\Mini Recommendation System"
    with open(f"{PATH}\\users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)



