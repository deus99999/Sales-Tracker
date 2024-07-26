import sys
from main import SalesRecorder


def main():
    print("Usage: python script.py <item> <quantity> <price>")
    if len(sys.argv) != 4:

        sys.exit(1)

    item = sys.argv[1]
    try:
        quantity = int(sys.argv[2])
        price = float(sys.argv[3])
    except ValueError as e:
        print("Quantity should be an integer and price should be a float.")
        sys.exit(1)

    recorder = SalesRecorder()
    #recorder.create_csv()
    recorder.add_sale( item, quantity, price)
    #recorder.add_sale('Guitar', 1, 2000)
    print(f"Sales data recorded in {recorder.filename}")


# Example usage
if __name__ == "__main__":
    main()