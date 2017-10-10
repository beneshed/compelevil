from bless.ssh.certificate_authorities.ssh_certificate_authority_factory import \
    get_ssh_certificate_authority
from bless.ssh.certificates.ssh_certificate_builder import SSHCertificateType
from bless.ssh.certificates.ssh_certificate_builder_factory import get_ssh_certificate_builder

import os

parent_dir = os.path.abspath(os.path.dirname(__file__))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
ggrandparent_dir = os.path.abspath(os.path.join(grandparent_dir, os.pardir))
ca_private_key = None
ca_private_key_password = 'password'

user_public_key = None
with open(os.path.join(os.path.join(ggrandparent_dir, 'example'), 'example-com-ca')) as textfile:
    ca_private_key = textfile.read()

with open(os.path.join(os.path.join(ggrandparent_dir, 'example'), 'user.pub')) as textfile:
    user_public_key = textfile.read()

ca_private_key_encoded = bytes(ca_private_key.encode())
ca_private_key_password_encoded = bytes(ca_private_key_password.encode())
user_public_key_encoded = bytes(user_public_key.encode())

ca = get_ssh_certificate_authority(ca_private_key_encoded, ca_private_key_password_encoded)

cert_builder = get_ssh_certificate_builder(ca, SSHCertificateType.USER,
                                           user_public_key_encoded)

print(cert_builder)