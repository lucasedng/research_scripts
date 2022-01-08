from request_lattices_data import (
    determinant_request_from_web,
    dimension_request_from_web,
    gram_matrix_request_from_web,
    kissing_number_request_from_web,
    minimal_norm_request_from_web,
    name_request_from_web
)
from requests import get
from json import dumps
from typing import List, Dict, Union


def dictionary_import(list_lattices: list) -> Dict[str, Dict]:

    dictionary = {}

    for lattice in list_lattices:
        response = get(
            f'https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/{lattice}.html'
        )

        site_return = str(response.content).replace('\\n', '')

        final_dict = {
            "name": name_request_from_web(site_return),
            "dimension": dimension_request_from_web(site_return),
            "determinant": determinant_request_from_web(site_return),
            "minimal_norm": minimal_norm_request_from_web(site_return),
            "kissing_number": kissing_number_request_from_web(site_return),
            "gram_matrix": gram_matrix_request_from_web(site_return),
        }

        dictionary[lattice] = final_dict

    return dictionary


def requested_lattices() -> List[str]:

    print('type the list of lattices you want (to finish type "end"). ')
    lattice = input()
    list_lattices = []
    while lattice.lower() != 'end':
        list_lattices.append(lattice)
        lattice = input()

    return list_lattices


def json_export(dictionary: dict) -> None:
    json_object = dumps(dictionary, indent=4)
    with open("lattices.json", "w") as outfile:
        outfile.write(json_object)

    return None


def main():

    json_export(dictionary_import(requested_lattices()))


if __name__ == "__main__":
    main()
