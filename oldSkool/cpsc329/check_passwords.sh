#!/bin/bash

# Define variables
USERNAMES=(
"AliA" "RayS" "eMcCor" "kya_lee" "rnyud"
"Asophigus" "Ricolapalola" "elifant" "kyalee" "ryabn"
"DakyW" "Subs" "enzo" "lexi459" "samra_shereen"
"FlameBanter" "Sylest" "erinung" "linuxbrew" "sean_tan"
"GioRapisarda" "WilliamSpencer" "hc332" "louize9" "shahadanA"
"HanzDelaCruz" "WinterBird" "hehe" "marwah" "simonoseen"
"HaydenDusyk" "Yasna" "henisnpatel" "matholimue" "singhranbir57"
"HussienA12" "Yuumi" "hpthegreat" "matiassalvador" "sramzan27"
"Jort" "ZainabM" "iamandy" "mcheatham" "swami"
"JuanPCF" "Zyad" "iangray" "meowmagic" "tamiade1"
"KuYiin" "ak" "jaskarankarwal" "minah" "tommybuckets"
"MM" "ammaarmelethil" "jenebs" "minoh" "ubuntu"
"MannPatel" "analauragrz" "joannadrs" "muhammad1738" "victorcampos"
"MikuEnjoyer" "asadm123" "jukmifgguggh" "mukha__" "vincent_tsin"
"NavpreetSingh" "ayman" "katarinad" "nathaniel" "waffle"
"Neeraj" "brandonsmith" "katrinac" "notTrilokAnish" "weihansong"
"Nick" "brians" "kaylee" "penguinlover123"
"Nicos" "derrickm" "kemmy" "reetghosh1"
"Nuncyy" "ducky" "kevinhoang9268" "remnant"
)

PASSWORD="cpsc2024"
HOST="ottersarecute.com"
REMOTE_FILE="changeyourpassword.txt"

# Loop through each username
for USERNAME in "${USERNAMES[@]}"; do
  # Use SSH to try to log in and create the file
  sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no "$USERNAME@$HOST" "echo 'Please change your password' > $REMOTE_FILE"

  # Check the exit status of the SSH command
  if [ $? -eq 0 ]; then
    echo "Password is correct for user $USERNAME, file created."
  else
    echo "Failed to login for user $USERNAME."
  fi
done

