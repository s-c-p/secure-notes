Secure (almost) Notes
=====================

a plug-in capable CLI app which lets you write and keep track of notes securely.

    Security Warning: OpenSSL writes decrypted files to disk and not to memory. Although every file is securely over-written by garbage, if some backup daemon is running in background, it may compromise your secrets.

Plug-in Architecture:
~~~~~~~~~~~~~~~~~~~~~

ux
  this makes the project really ambitious and forces me to think with more abstraction. `ux` plug-in will handle, well user experience stuff

crypto
  know path of ``crypto_executable`` and know the ``encryption_string``, ``decryption_string`` and their associated variables for a given ``crypto_executable``

backup
  know path of ``backup_executable`` and know the ``backup_string`` and its associated variables for a given ``backup_executable``

crypto-transfer
  to migrate entire repo from one crypto client to another

backup-transfer
  to migrate entire repo from one backup client to another


Usage:
~~~~~~

::

    py secure-notes.py -h


Don't copy.
