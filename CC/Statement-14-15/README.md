## VM 1

      username:vagrant
      password:vagrant

      ifconfig // note inet address


## VM 2

      username:vagrant
      password:vagrant

      ifconfig // note inet address

## VM 1

      ping <ip of vm2>
      touch transfer.txt
      nano transfer.txt
      //write content->Press Ctr X -> Y -> Enter
      cat transfer.txt
      scp transfer.txt vagrant@<ip of 2nd vm>:/home/vagrant

## VM 2

      ls //to see the transfered file from vm1

### Note: If command ifconfig is not found then

      sudo apt install net-tools
