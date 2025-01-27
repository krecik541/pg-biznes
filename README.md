# Biznes Elektroniczny: Konfiguracja i Wdrożenie PrestaShop

## Opis projektu

Celem projektu jest praktyczna nauka pracy z oprogramowaniem Open Source dedykowanym do tworzenia sklepów internetowych. W trakcie realizacji zapoznaliśmy się z konfiguracją i dostosowaniem platformy PrestaShop do wymagań klienta, a następnie przygotowaliśmy środowisko wdrożeniowe i uruchomiliśmy rozwiązanie w dedykowanej infrastrukturze.

Realizacja projektu ma na celu:
- Przybliżenie warunków pracy programisty w rzeczywistych projektach.
- Zaznajomienie z procesem dostosowania istniejących narzędzi do potrzeb klienta.
- Udoskonalenie umiejętności pracy w zespole, zarządzania kodem źródłowym oraz wdrożenia rozwiązania na produkcję.

Projekt umożliwia zdobycie praktycznej wiedzy z zakresu:
- Wykorzystania repozytorium kodu źródłowego.
- Pracy z cudzym kodem źródłowym i dokumentacją techniczną.
- Wirtualizacji i konteneryzacji podczas tworzenia środowiska developerskiego.
- Konfiguracji serwerów i orkiestracji kontenerów.
- Automatyzacji testów oraz konfiguracji narzędzi analitycznych.

---

## Wykorzystane oprogramowanie

Do realizacji projektu wykorzystaliśmy:

* **Platforma sklepu internetowego**: PrestaShop 1.7.8 [Repozytorium PrestaShop](https://github.com/PrestaShop/PrestaShop/tree/1.7.8.x)

* **Narzędzia developerskie**:  
   - Repozytorium kodu: [GitHub](https://github.com)
   - System kontroli wersji: [Git](https://git-scm.com)  
   - Edytor kodu: [Visual Studio Code](https://code.visualstudio.com) 

* **Środowisko uruchomieniowe**:  
   - System konteneryzacji: [Docker](https://docker.com)  
   - System zarządzania kontenerami: [Docker Compose](https://docs.docker.com/compose/)  

* **Dodatkowe oprogramowanie**:  
   - Serwer: Apache (httpd2), MySQL (MariaDB)
   - Biblioteki PHP: `php`, `php-mysql`, `php-pdo`, i inne wymagane przez PrestaShop.
   - Narzędzie do testów UI: [Selenium](https://www.selenium.dev/documentation/en/)

---

## Sposób uruchomienia

### 1. Przygotowanie środowiska developerskiego

1. **Klonowanie repozytorium projektu**:
   ```bash
   git clone https://github.com/piotreuszxx/pg-biznes.git
   cd <NAZWA_FOLDERU>
   ```

2. **Uruchomienie środowiska kontenerowego**:
   - Zainstaluj Docker i Docker Compose.
   - Uruchom kontenery za pomocą:
     ```bash
     docker-compose up -d
     ```

3. **Dostosowanie sklepu**:
   - Zaloguj się do panelu administracyjnego PrestaShop.
   - Zmień ustawienia zgodnie z wymaganiami projektu.

4. **Testowanie aplikacji**:
   - Uruchom skrypt `testy.py` wykorzystujący bibliotekę Selenium.

### Wdrożenie środowiska produkcyjnego

1. Skonfiguruj docelowy serwer produkcyjny.
2. Skopiuj pliki i konfigurację na serwer za pomocą `scp` lub innego narzędzia.
3. Zainstaluj i uruchom kontenery w środowisku produkcyjnym.

---

## Skład zespołu

- Tymon Muszyński
- Piotr Przymus
- Maciej Szymczak
- Mateusz Merda
