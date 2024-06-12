# main.py
import argparse
import json
from funny_json_explorer import FunnyJsonExplorer
from factory import TreeFactory , RectangleFactory
from icon_family import ChessIconFamily, SmileIconFamily

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a description of the script.")
    parser.add_argument("--filename", "-f", type=str, help="the JSON file to be explored")
    parser.add_argument("--style", "-s", type=str, default="tree", help="explor style (tree/rectangle)")
    parser.add_argument("--icon", "-i", type=str, default="space", help="icon family (chess/smile)")
    args = parser.parse_args()
    filename = args.filename
    with open(filename) as json_file:
        json_data = json.load(json_file)

    icon_families = [ChessIconFamily(), SmileIconFamily()]

    current_icon_family = icon_families[0]
    for icon_family in icon_families:
        if icon_family.name == args.icon:
            current_icon_family = icon_family

    factories = [RectangleFactory(current_icon_family),TreeFactory(current_icon_family)]       

    current_factory = factories[0]
    for factory in factories:
        if factory.name == args.style:
            current_factory = factory

    explorer = FunnyJsonExplorer( current_factory )
    explorer.show(json_data)
    print("\n")
    


    '''
    for icon_family in icon_families:
        print(f"Using icon family: {icon_family.__class__.__name__}")

        print("Tree Style:")
        explorer = FunnyJsonExplorer(TreeFactory(icon_family))
        explorer.show(json_data)
        print("\n")

        print(f"Using icon family: {icon_family.__class__.__name__}")

        print("Rectangle Style:")
        explorer = FunnyJsonExplorer(RectangleFactory(icon_family))
        explorer.show(json_data)
        print("\n")
    '''