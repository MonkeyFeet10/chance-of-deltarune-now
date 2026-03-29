set -e
mkdir -p "Deltarune Tomorrow"
cp src/main.py "Deltarune Tomorrow"/main.py
cp -r assets/* "Deltarune Tomorrow"/
python -m pygbag --icon "Deltarune Tomorrow"/favicon.ico --build "Deltarune Tomorrow"/main.py
rm -rf docs/
mkdir docs/
mv "Deltarune Tomorrow"/build/web/* "docs/"
rm -rf "Deltarune Tomorrow"
python src/patch.py
python -m http.server --directory docs/ -b 127.0.0.1 8000