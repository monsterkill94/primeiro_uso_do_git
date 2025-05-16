import argparse
from youtube_dl import YoutubeDL
import shlex  # Para escapar caracteres especiais no shell

def download_video(url, format="18"):
    """
    Downloada um vídeo da URL com qualidade alta.
    
    Args:
        url (str): A URL do vídeo no YouTube.
        format (str, optional): O formato para download. Padrão é "18" para 1080p.
    """
    # Configurar as opções do youtube-dl
    ydl_opts = {
        'format': format,
        '-r': 'worst',  # Prioridade de qualidade mais alta
        '-k': '250',  # Limita o tamanho do arquivo em MB
        'keepalive': True,  # Mantém a conexão após iniciar o download
        'max_retries': 3,  # Tenta novamente após falhas
    }
    
    # Construir a comando de download
    dl_command = f"youtube-dl -o {shlex.quote(f'"{url}"')} '{{{url}}}'"
    print(f"Iniciando o download: {dl_command}")
    
    # Executar o comando na shell
    subprocess.call(dl_command, shell=True, check=True)

def main():
    parser = argparse.ArgumentParser(description='Download de música com alta qualidade do YouTube')
    parser.add_argument('url', help='URL do vídeo no YouTube')
    parser.add_argument('--quality', 
                       choices=['480p', '720p', '1080p', '4k'],
                       help='Qualidade do vídeo para download')
    parser.add_argument('--extract-audio', action='store_true',
                       help='Download apenas o áudio da música')
    
    args = parser.parse_args()
    
    try:
        if args.extract_audio:
            format_number = 137  # 720p é comumente usado para áudios de boa qualidade
        else:
            if args.quality in ['480p', '720p', '1080p', '4k']:
                quality_map = {
                    '480p': 22,
                    '720p': 137,
                    '1080p': 18,
                    '4k': 251,
                }
                format_number = quality_map[args.quality]
            else:
                raise argparse.ArgumentError(f"'--quality' deve ser um dos valores: {', '.join(['480p', '720p', '1080p', '4k'])}'")
        
        download_video(args.url, f"-{format_number}best")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao downloadar o vídeo. Motivo: {e.stderr}")

if __name__ == "__main__":
    main()
