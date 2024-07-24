from abc import ABC, abstractmethod


# INTERFACE
class FormatoAudio(ABC):
    @abstractmethod
    def abrir(self, s: str) -> None: 
        pass

    @abstractmethod
    def reproduzir(self) -> None: 
        pass

    @abstractmethod
    def parar(self) -> None: 
        pass

# CONCRETA 
class Mp3Play(FormatoAudio):
    def __init__(self) -> None:
        self.s = None

    def abrir(self, s: str) -> None: 
        self.s = s
        print(f"(MP3) Abrindo o arquivo {self.s}")

    def reproduzir(self) -> None: 
        print(f"(MP3) Reproduzindo o arquivo {self.s}")

    def parar(self) -> None: 
        print(f"(MP3) Fechando o arquivo {self.s}")

# CONCRETA 
class WavPlay(FormatoAudio):
    def __init__(self) -> None:
        self.s = None

    def abrir(self, s: str) -> None: 
        self.s = s
        print(f"(WAV) Abrindo o arquivo {self.s}")

    def reproduzir(self) -> None: 
        print(f"(WAV) Reproduzindo o arquivo {self.s}")

    def parar(self) -> None: 
        print(f"(WAV) Fechando o arquivo {self.s}")

# CONCRETA 
class WmaPlay:
    def __init__(self) -> None:
        self.s = None
        self.n = None

    def set_file(self, s: str) -> None:
        self.s = s
        print(f"(WMA) Definindo arquivo {self.s} para reprodução")
    
    def open(self) -> None:
        print(f"(WMA) Abrindo o arquivo {self.s}")

    def set_location(self, n: int) -> None:
        self.n = n
        print(f"(WMA) Reprodução do arquivo {self.s} vai ser iniciada na posição {self.n}")

    def play(self) -> None:
        print(f"(WMA) Reproduzindo arquivo {self.s} a partir da posição {self.n}")

    def stop(self) -> None:
        print(f"(WMA) Parando reprodução do arquivo {self.s}")

# ADAPTADOR
class AdaptadorWmaPlay(FormatoAudio):
    def __init__(self) -> None:
        self.wma: WmaPlay = WmaPlay()

    def abrir(self, s: str) -> None: 
        print("(WMA ADAPTADA) executando método 'abrir'")
        self.wma.set_file(s)
        self.wma.open()
        self.wma.set_location(0)

    def reproduzir(self) -> None: 
        print("(WMA ADAPTADA) Executando método 'reproduzir'")
        self.wma.play()

    def parar(self) -> None: 
        print("(WMA ADAPTADA) Executando método 'parar'")
        self.wma.stop()

s1 = "audio1.mp3"
s2 = "audio2.wav"
s3 = "audio3.wma"
print(f"Os seguintes arquivos de áudio serão reproduzidos:")
print(s1)
print(s2)
print(s3)
print()
print("Instanciando objetos Mp3Play, WavPlay e AdaptadorWmaPlay")
print()
mp3 = Mp3Play()
wav = WavPlay()
wma = AdaptadorWmaPlay()
print("Criando uma lista com os objetos instanciados, como se fosse uma fila das músicas a serem tocadas.")
print("Como o laço que vai iterar a lista espera objetos FormatoAudio, ele vai conseguir reproduzir o WMA")
print()
arquivos = [s1, s2, s3]
audios = [mp3, wav, wma]

i = 0
for audio in audios:
    audio.abrir(arquivos[i])
    audio.reproduzir()
    audio.parar()
    print()
    i += 1