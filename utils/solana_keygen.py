from solders.keypair import Keypair
import base58

class SolanaKeyGenerator:
    """
    Handles the generation and management of Solana keypairs.

    This class provides functionality to generate new Solana keypairs,
    access the public key (address), and retrieve the private key in
    base58 encoded format for easy storage and use in Solana-based applications.
    """

    def __init__(self):
        """
        Initialize the SolanaKeyGenerator instance.

        Attributes:
            keypair (Keypair or None): Stores the generated Solana keypair object.
                                       Initially set to None until a keypair is generated.
        """
        self.keypair = None

    def generate_new_keypair(self):
        """
        Generate a new Solana keypair.

        This method creates a new cryptographic keypair using the `solders` library
        and assigns it to the instance attribute `self.keypair`.

        Returns:
            SolanaKeyGenerator: The current instance of the generator for method chaining.

        Example:
            >>> generator = SolanaKeyGenerator()
            >>> generator.generate_new_keypair()
            <SolanaKeyGenerator object>
        """
        self.keypair = Keypair()
        return self

    @property
    def public_key(self):
        """
        Retrieve the public key (address) of the generated keypair.

        The public key is returned as a base58-encoded string, which is the standard
        representation of public keys on the Solana blockchain.

        Returns:
            str: The base58-encoded public key.

        Example:
            >>> generator = SolanaKeyGenerator()
            >>> generator.generate_new_keypair()
            >>> generator.public_key
            '3n3f5gFWzQmr1BRkgLXZWzFzK9V1NcXTujHobkrPXjwa'
        """
        if self.keypair is None:
            raise ValueError("No keypair generated. Please call generate_new_keypair() first.")
        return str(self.keypair.pubkey())

    @property
    def private_key_base58(self):
        """
        Retrieve the private key of the generated keypair in base58-encoded format.

        The private key is securely encoded in base58, providing a compact and
        human-readable format for storing and using private keys in Solana applications.

        Returns:
            str: The base58-encoded private key.

        Example:
            >>> generator = SolanaKeyGenerator()
            >>> generator.generate_new_keypair()
            >>> generator.private_key_base58
            '3aXqHioP8KCBRTzudm3JXsQs9J4kAf5tHXsQmYx9tmGA'
        """
        if self.keypair is None:
            raise ValueError("No keypair generated. Please call generate_new_keypair() first.")
        return base58.b58encode(self.keypair.secret()).decode("ascii")


def generate_solana_wallet():
    """
    Generate and return a new Solana wallet.

    This is a utility function that instantiates the `SolanaKeyGenerator` class,
    generates a new keypair, and returns the generator instance. It simplifies
    wallet generation for quick and easy use.

    Returns:
        SolanaKeyGenerator: An instance of `SolanaKeyGenerator` with a generated keypair.

    Example:
        >>> wallet = generate_solana_wallet()
        >>> wallet.public_key
        '9G3iq2UC9Xa1sfU5DiGwNf7oeRugQvrD1Wn6hKQHFk8Y'
        >>> wallet.private_key_base58
        '5xW9XThBbReiGhys4HJzZYLBHStztd9yTTqf2HwF6Pwq'
    """
    generator = SolanaKeyGenerator()
    generator.generate_new_keypair()
    return generator
