import bs4, requests


if __name__ == '__main__':
    paparser = argparse.ArgumentParser(description='Extract')
    parser.add_argument('first_number', type=float)
    parser.add_argument('second_number', type=float)
    parser.add_argument('third_number', type=float)
    args = parser.parse_args()
    result = maximumAbsoluteOfThree(args.first_number, args.second_number, args.third_number)
    print(result)