Oznaczenie wybranych technik:
   1 - zero-shot
   2 - few-shot
   3 - Role prompting

Co każdy z technik promtów ma zapisany przykład interpretacji albo nie posiada go:
1 model dostaje wyłącznie pytanie, bez przykładów i dodatkowych instrukcji.
* 2 model ma przykład "<przyklady>\n"
            "Pytanie: Jaka jest stolica Francji?\n"
            "Odpowiedź: Paryż\n\n"
            "Pytanie: Jaka jest stolica Japonii?\n"
            "Odpowiedź: Tokio\n"
            "</przyklady>\n\n".
3 model ma przykład "<rola>Jesteś światowej klasy ekspertem w tej dziedzinie.</rola>.


* [W technice 2 celowo zastosowano przykłady dotyczące innego zadania (pytania o stolice państw), a nie podsumowywania artykułów. Celem było sprawdzenie, czy model wykorzysta sam fakt otrzymania przykładów i przeniesie sposób odpowiedzi na nowe zadanie.]


Cel: jak każdy z technik prompt interpretuje tekst.

************************************************************************************************************************************************************************************************


***************************************Test 1

Opowiedź zapisana tylko "podsumuj artykuł Sowy to zróżnicowana grupa drapieżnych ptaków.".

odpowiedzi:

    Technika 1:
        Claude: 
# Podsumowanie artykułu: "Sowy to zróżnicowana grupa drapieżnych ptaków"

## Główna teza
    Sowy stanowią zróżnicowaną grupę ptaków drapieżnych o specjalistycznych adaptacjach do polowania.

## Kluczowe informacje:

**Charakterystyka sów:**
- Są ptakami drapieżnymi
- Wykazują znaczne zróżnicowanie morfologiczne
- Posiadają specjalne przystosowania do aktywności nocnej

**Cechy adaptacyjne:**
- Duże, frontalnie umieszczone oczy przystosowane do widzenia w mroku
- Asymetryczne umieszczenie uszu ułatwiające lokalizację zdoby
    
    Technika 2:
        Claude: 
# Podsumowanie artykułu: "Sowy to zróżnicowana grupa drapieżnych ptaków"

Artykuł podkreśla, że sowy stanowią zróżnicowaną grupę ptaków drapieżnych o specjalistycznych adaptacjach do polowania, szczególnie w warunkach nocnych. Charakteryzują się unikalnymi cechami morfologicznymi i behawioralnymi, które umożliwiają im efektywne funkcjonowanie jako nocne myśliwce.

    Technika 3:
        Claude: 
# Podsumowanie artykułu: "Sowy to zróżnicowana grupa drapieżnych ptaków"

## Główna teza
Sowy reprezentują zróżnicowaną grupę ptaków drapieżnych o szerokim spektrum adaptacji ekologicznych i morfologicznych.

## Kluczowe aspekty

**Zróżnicowanie taksonomiczne i morfologiczne**
- Sowy stanowią heterogeniczną grupę w obrębie rzędu Strigiformes
- Wykazują znaczną zmienność wielkości, budowy ciała i cech morfologicznych
- Różnorodność umożliwia specjalizację w różnych niszach ekologicznych

**Adaptacje do roli drapieżnika**
- Wyspecjalizowane prz


***************************************test 2


Opowiedź zapisana tylko "podsumuj artykuł Sowy z powodu nocnego trybu życia są bardzo skrytymi i mało rzucającymi się w oczy ptakami. W naszym kraju mamy aż 13 gatunków tych ptaków, z których 9 regularnie gnieździ się w Polsce.

Najpospolitszą sową całej Europy jest puszczyk zwyczajny, który spotykany jest w wielu środowiskach również w naszym kraju. Spotkać go można od niedostępnych obszarów górskich, po centra dużych miast. Puszczyki świetnie zaadaptowały się do życia na terenach zurbanizowanych i nie przeszkadza im bliska obecność ludzi. Są jednocześnie bardzo pożytecznymi ptakami, gdyż polują na gryzonie nawet wielkości szczura.

Puszczyki naturalnie gnieżdżą się w dużych dziuplach starych drzew, bądź zajmują opuszczone gniazda innych dużych ptaków, jak kruków, krogulców czy myszołowów. Na terenach zamieszkałych przez człowieka zakładają gniazda w wieżach kościelnych czy stodołach, a także chętnie zajmują specjalne budki dla sów.

Zachowania rozrodcze ptaki te zaczynają przejawiać już jesienią, kiedy w październiku i listopadzie sowy wyszukują miejsc gniazdowych, walczą o terytorium i ustalają granice swoich rewirów. Od grudnia do lutego trwają zaloty, podczas których samce zalecają się do samic i tworzą ze swoimi wybrankami monogamiczne pary.

Samce wykonują tańce godowe i zdobywają swoją przyszłą partnerkę przynosząc jej upolowane gryzonie. Po utworzeniu się par, puszczyki przystępują do lęgów. Czynią to bardzo wcześnie, bo już w marcu, a na terenach miejskich, jeśli pogoda jest sprzyjająca nawet na początku lutego. Po kopulacji samica składa od jednego do pięciu jaj w odstępach dwudniowych. Klucie piskląt jest więc niesynchroniczne, dzięki czemu przy niedostatku pokarmu przeżywają tylko najstarsze i najsilniejsze.

Jaja puszczyka są barwy białej i owalnego kształtu o wymiarach 4 x 5 cm. Inkubacja ich trwa niecały miesiąc i są w jej czasie wysiadywane wyłącznie przez samicę. Partner w tym czasie poluje i przynosi jej pożywienie. Pisklęta po wylęgu przez pierwszy tydzień przebywają stale z matką, a następnie również ona rusza na łowy, aby wspomóc samca w wykarmieniu coraz większych i żarłoczniejszych młodych.

Autor: Cezary Korkosz".

odpowiedzi:

    Technika 1:
        Claude: 
# Podsumowanie artykułu "Sowy"

    Artykuł omawia charakterystykę i biologię puszczyka zwyczajnego, najpospolitszej sowy w Europie i w Polsce.

## Główne punkty:

**Obecność w Polsce:**
- W kraju mieszka 13 gatunków sów, z czego 9 regularnie się gnieździ
- Puszczyk zwyczajny występuje wszędzie – od gór po miasta

**Przystosowanie i rola w ekosystemie:**
- Dobrze zaadaptowały się do życia w miastach
- Polują na gryzonie, w tym szczury – są pożyteczne dla człowieka

**Miejsca gnieżdżowania:**
- Naturalnie: duże
    
    Technika 2:
        Claude: 
# Podsumowanie artykułu: "Sowy z powodu nocnego trybu życia..."

## Sowy w Polsce
- W Polsce występuje **13 gatunków sów**
- **9 gatunków** regularnie gnieździ się w kraju
- Ze względu na nocny tryb życia są ptakami skrytymi i mało widocznymi

## Puszczyk zwyczajny
- Najpospolitszy gatunek sowy w Europie
- Zamieszkuje różne środowiska – od gór do miast
- Doskonale zaadaptował się do terenów zurbanizowanych
- Poluje na gryzonie, w tym szczury

## Gnieżdżenie się
- Naturalne nory: duże dziuple starych drzew, opus

    Technika 3:
        Claude: 
# Podsumowanie artykułu: "Sowy z powodu nocnego trybu życia..."

## Biogeografia i występowanie
- W Polsce stwierdzono **13 gatunków sów**, z czego **9 regularnie gnieździ się**
- Nocny tryb życia czyni je ptakami diskretnymiMi i trudnymi do obserwacji
- **Puszczyk zwyczajny** – najpospolitszy gatunek w Europie, o największej plastyczności ekologicznej

## Plastyczność ekologiczna puszczyków
- Zamieszkują środowiska od terenów górskich do miast
- Doskonale zaadaptowali się do urbanizacji
- Tolerują bliską sąsiedztwo człowieka


***************************************test 3


Opowiedź zapisana tylko "podsumuj artykuł Sowa: charakterystyka, mity, dźwięk i nie tylko
Sowy to nocne, mięsożerne ptaki drapieżne, znane z cichego lotu i zwyczajów łowieckich.
Rozmnażają się wiosną i wykorzystują opuszczone gniazda innych ptaków do składania jaj.
Ich dieta różni się w zależności od gatunku i obejmuje gryzonie, owady, ryby i jaszczurki.
Sowy są narażone na kłusownictwo, zatrucia i niszczenie siedlisk.".

odpowiedzi:

    Technika 1:
        Claude: 
# Podsumowanie artykułu: "Sowa: charakterystyka, mity, dźwięk i nie tylko"

## Główne cechy sów
- Nocne, mięsożerne ptaki drapieżne
- Charakteryzują się cichym lotem i efektywnością łowiecką

## Rozmnażanie
- Okres godowy przypadający na wiosnę
- Wykorzystywanie opuszczonych gniazd innych ptaków do składania jaj

## Dieta
- Różnorodna w zależności od gatunku
- Obejmuje: gryzonie, owady, ryby i jaszczurki

## Zagrożenia
- Kłusownictwo
- Zatrucia
- Niszczenie siedlisk naturalnych

    Technika 2:
            Claude: 
# Podsumowanie artykułu: "Sowa: charakterystyka, mity, dźwięk i nie tylko"

## Charakterystyka
- Nocne, mięsożerne ptaki drapieżne
- Znane z cichego lotu i efektywnych umiejętności łowieckich

## Rozmnażanie
- Rozmnażają się wiosną
- Wykorzystują opuszczone gniazda innych ptaków do składania jaj

## Dieta
- Zróżnicowana w zależności od gatunku
- Obejmuje: gryzonie, owady, ryby i jaszczurki

## Zagrożenia
- Kłusownictwo
- Zatrucia
- Niszczenie siedlisk naturalnych

    Technika 3:
        Claude: 
# Podsumowanie artykułu: "Sowa: charakterystyka, mity, dźwięk i nie tylko"

## Charakterystyka morfologiczna i behawioralna
- **Nocne ptaki drapieżne** o diecie mięsożernej
- Wyróżniają się **cichym lotem** – wynik specjalnych adaptacji piórkowych (zębate brzegi piór)
- Posiadają wysoce wyspecjalizowane umiejętności łowieckie

## Strategie rozrodcze
- **Sezon rozrodczy**: wiosna
- **Taktyka gniazdowania**: wykorzystanie opuszczonych gniazd innych ptaków (parasityzm gniezdowy)
- Efektywna strategia reprodukcyjna

************************************************************************************************************************************************************************************************

Wyniki testów:
    test 1: 
        technika 1:
        - Model znacznie rozbudował odpowiedź.
        - Dodał informacje o przystosowaniach do życia nocnego, budowie ciała i polowaniu, których nie było w tekście.
        technika 2:
        - Odpowiedź była krótsza niż w Zero-shot, ale również zawierała dodatkową wiedzę spoza artykułu.
        technika 3:
        - Model użył najbardziej specjalistycznego języka.
        - Pojawiły się pojęcia takie jak „Strigiformes”, „nisze ekologiczne” czy „adaptacje morfologiczne”, których nie było w tekście.
### Wniosek
Przy bardzo krótkim tekście wszystkie techniki uzupełniały brakujące informacje własną wiedzą modelu. Największe rozszerzenie odpowiedzi nastąpiło po zastosowaniu Role Prompting.

    test 2:
        technika 1:
        - Powstało poprawne podsumowanie najważniejszych informacji.
        - Model zachował główne fakty dotyczące występowania, gniazdowania i rozmnażania.
        technika 2:
        - Odpowiedź była bardziej uporządkowana.
        - Informacje podzielono na sekcje i wypunktowania.

        technika 3:
        - Model zastosował bardziej naukowe nazwy, np. „biogeografia”, „plastyczność ekologiczna”.
        - Styl był bardziej formalny niż w pozostałych technikach.
### Wniosek

Przy dłuższym artykule wszystkie techniki poprawnie streszczały treść. Różnice dotyczyły głównie stylu odpowiedzi i poziomu specjalistycznego słownictwa.

    test 3:
        technika 1:
        - Podsumowanie wiernie odzwierciedlało treść artykułu.
        - Zachowano wszystkie najważniejsze informacje.
        technika 2:
        - Wynik był zbliżony do Zero-shot.
        - Zmienił się jedynie sposób sformułowania zdań.
        technika 3:
        - Model ponownie zastosował język ekspercki.
        - Dodał wyjaśnienie dotyczące budowy piór oraz użył określenia „pasożytnictwo gniazdowe”, którego nie było w tekście.
### Wniosek

Role Prompting ponownie spowodował dodawanie wiedzy spoza artykułu. Zero-shot i Few-shot pozostały bliższe oryginalnej treści.

### Podsumowanie ###
Największe różnice między technikami były widoczne przy bardzo krótkim tekście (Test 1). W przypadku dłuższych artykułów (Test 2 i Test 3) wszystkie techniki poprawnie identyfikowały najważniejsze informacje, a różnice dotyczyły przede wszystkim stylu odpowiedzi.Technika 1 dobrze radzi sobie z prostym podsumowaniem tekstu i zwykle pozostaje blisko treści źródłowej. Technika 2 w wykonanych testach wpływał głównie na uporządkowanie odpowiedzi, a nie na jej zawartość. Technika 3 miał największy wpływ na wynik. Model używał bardziej formalnego i specjalistycznego języka oraz częściej rozszerzał odpowiedź o wiedzę spoza artykułu. 

Wyniki pokazały, że model poprawnie wykonał polecenie podsumowania artykułu, jednak różnice względem techniki 1 były niewielkie. Odpowiedzi były nieco bardziej uporządkowane, ale przykłady z innej dziedziny nie wpłynęły znacząco na treść podsumowania. Oznacza to, że przykłady użyte w technice 2 są najbardziej skuteczne wtedy, gdy są zbliżone do zadania, które model ma wykonać.
