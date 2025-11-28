# def students_file():
#     sample_names=[
#         "Sriparna Roy",
#         "Ayushi Chakraborty",
#         "Ankur Chakraborty",
#         "Tuneer Paul"
#     ]
#     with open ("students_cert.txt","w") as f:
#         for name in sample_names:
#             f.write(name+"\n")
#
#     print("students file created")


def generate_certificates():
    with open("students_cert.txt", "r") as f:
        students = f.readlines()

    for line in students:
        name = line.strip()
        if not name:
            continue

        safe_name = name.replace(" ", "__")
        filename = f"certificate_{safe_name}.txt"
        certificate_text = f"""
        This is to certify that
              {name}
        has successfully completed the course
        """


        with open(filename, "w") as cert_file:
            cert_file.write(certificate_text.strip())

        print(f"Certificate file created for {name}")


if __name__ == "__main__":
    generate_certificates()



