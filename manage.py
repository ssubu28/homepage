# Python script to generate a static site

import utils
import sys


if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print("\nPlease refer to the instructions below.")
        print("Usage:")
        print("\tRebuild site:    python manage.py build")
        print("\tCreate new page: python manage.py new")
    else:
        if sys.argv[1] == "build":
            utils.main()
        elif sys.argv[1] == "new":
            utils.newpage_generator()
        else:
            print("\nPlease refer to the instructions below.")
            print("Usage:")
            print("\tRebuild site:    python manage.py build")
            print("\tCreate new page: python manage.py new\n")
            print("Provide a command after filename to run - build or new\n")
