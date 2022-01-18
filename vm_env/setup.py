import os
import re
import webbrowser

user_home_dir = os.path.join(os.path.sep, "/usr/home", "administrator")

# Defining main function
def main():
    print("#########################################")
    print("    Welcome to the automation VM setup")
    print("#########################################")
    print("GIT Setup:")
    username, email = get_git_creds()

    git_username_cmd = 'git config --global user.name "' + username + '"'
    git_email_cmd = 'git config --global user.email "' + email + '"'
    
    print("Setting GIT username...")
    stream = os.popen(git_username_cmd)
    output = stream.read()
    print(output)
    
    print("Setting GIT email...")
    stream = os.popen(git_email_cmd)
    output = stream.read()
    print(output)
    
    print("Git configuration...")
    git_list_cmd = "git config --list"
    stream = os.popen(git_list_cmd)
    output = stream.read()
    print(output)
    
    print("SSH Key Setup:")
    already_have_ssh_key_question = yes_or_no_question("Do you already have SSH keys for Github.com/extremenetworks or Github.extremenetworks.com?")

    if already_have_ssh_key_question:
        ssh_key_question = yes_or_no_question("Did you copy your ssh keys to a known location on this VM?")
        create_new_directory(os.path.join(user_home_dir, '.ssh'))
        if ssh_key_question:
            
            # We have keys just copy them to .ssh
            private_key, public_key = get_ssh_key_files()

            keys_found = False
            if os.path.isfile(public_key) and os.path.isfile(private_key):
                public_key_name = "id_ed25519.pub"
                private_key_name = "id_ed25519"
                if public_key_name in public_key and private_key_name in private_key:
                    keys_found = True
                else:
                    public_key_name = "id_rsa.pub"
                    private_key_name = "id_rsa"
                    if public_key_name in public_key and private_key_name in private_key:
                        keys_found = True

            if keys_found == False:
                print("Error: Unable to find acceptable ssh key files (id_ed25519.pub, id_ed25519, id_rsa.pub or id_ras)")
                exit(1)

            move_public_key_cmd = "mv " + public_key + ' ' + os.path.join(user_home_dir, '.ssh', public_key_name)
            stream = os.popen(move_public_key_cmd)
            output = stream.read()
            print(output)

            move_private_key_cmd = "mv " + private_key + ' ' + os.path.join(user_home_dir, '.ssh', private_key_name)
            stream = os.popen(move_private_key_cmd)
            output = stream.read()
            print(output)

            print("Setting permissions...")
            permission_list_cmd = "chmod 600 /usr/home/administrator/.ssh/*"
            stream = os.popen(permission_list_cmd)
            output = stream.read()
            print(output)

        else:
            print(" ERROR: You will need to copy over your ssh key files to this VM and rerun the script ")
            exit(1)
    else:
        print("Since you don't have ssh keys for Github.com/extremenetworks or Gibhub.extremenetworks.com we can generate those for you.")
        press_enter_to_continue("Would you like to continue and create your ssh keys (press enter to continue)?")
        create_new_directory(os.path.join(user_home_dir, '.ssh'))
        create_ssh_key_cmd = 'ssh-keygen -t ed25519 -C ' + email
        os.system(create_ssh_key_cmd)
        public_file = open(os.path.join(user_home_dir, '.ssh', 'id_ed25519.pub'), "r")
        press_enter_to_continue("This is your public key. This key will be needed for github. (press enter to continue)")
        print("SSH Public Key: \n")
        print("**************************************\n\n")
        print(public_file.read())
        print("\n\n**************************************")
        print("To access the repositories you will need to create a GitHub.com account. ")
        print("To start the process please send a request to helptools@extremenetworks.com for a GitHub.com account.")
        press_enter_to_continue("(press enter to continue)")
        print("Opening browser with directions on how to add the ssh key to Github and Github.com.")
        print("The first tab will have the directions on how to add the ssh key to github.")
        print("The second tab will be to github.extremenetworks.com.")
        print("The third tab will be to github.com/extremenetworks.")
        print("Please add your ssh key to both sites in order to ensure you will have access to all of the automation repositories.")
        print("NOTE: On GitHub.com you will also need to 'Enable SSO' after you add your public key")
        press_enter_to_continue("(press enter to continue)")
        webbrowser.open('https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account', new=2)
        webbrowser.open_new_tab('https://github.extremenetworks.com/')
        webbrowser.open_new_tab('https://github.com/extremenetworks')

    print("Completed")
    
    
def create_new_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_git_creds():

    git_creds_not_loaded = True
    while git_creds_not_loaded:
        username = input("Please enter in your git username: ")
        email = input("Please enter in your email: ")

        username_good = False
        email_good = False

        if check_email(email):
            email_good = True
        else:
            print("ERROR: Email: " + email + " is not valid")

        if username != "":
            username_good = True
        else:
            print("ERROR: User name can't be blank")

        if username_good and email_good:
            git_creds_not_loaded = False

    return username, email


def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if email != "":
        if re.search(regex, email):
            return True
        else:
            return False
    else:
        return False


def get_ssh_key_files():
    ssh_file_not_loaded = True

    while ssh_file_not_loaded:
        private_key = input("Please enter in path (including the file name) to the private key: ")
        public_key = input("Please enter in path (including the file name) to the public key: ")

        public_key_good = False
        private_key_good = False

        if os.path.exists(private_key) and not os.path.isdir(private_key):
            private_key_good = True
        else:
            print("ERROR: Private Key File: " + private_key + " doesn't exist")

        if os.path.exists(public_key) and not os.path.isdir(public_key):
            public_key_good = True
        else:
            print("ERROR: Public Key File: " + public_key + " doesn't exist")

        if private_key_good and public_key_good:
            ssh_file_not_loaded = False

    return private_key, public_key


def yes_or_no_question(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def press_enter_to_continue(statement):
    input(statement)

if __name__ == "__main__":
    main()
