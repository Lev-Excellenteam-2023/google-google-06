from data_extraction.data_extraction import extract_data


def main():
    d = extract_data(r'../Test/txt_files_for_tests')
    print(d)


if __name__ == '__main__':
    main()
