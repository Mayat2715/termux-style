B
    �o,]U
  �               @   s�   d dl Z d dlZd dlZd dlmZ d dlmZ	 dZ
dd� Zdd� Zd	d
� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zxe�  e�  q�W e�  dS )�    N)�choice)�sleep)z[0;1mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mc               C   s   t d� t�d� d S )Nzd



































































































�clear)�print�os�system� r   r   �main.py�cls   s    r
   c             C   s&   t �� }| |krt| d��� S d S d S )N�r)r   �listdir�open�read)�name�lsr   r   r	   �check   s    r   c               C   s   t tt�� d�� t�  d S )Nz/Github: https://github.com/Mayat2715
Versi: 3.2)r   �c�w�exitr   r   r   r	   �last   s    r   c              C   sb   d} d}xTt d�D ]H}ttt�d | |  d dd� |t| �d k rN|d nd}td	� qW d S )
Nz\|/-r   �   �[z] Tunggu sebentar�)�end�   g�������?)�ranger   r   r   �len�slp)Zhm�a�ir   r   r	   �lod   s     r    c             C   s"   t �  t�d| � d|� d�� d S )Nzcp "z" $HOME/.termux/z; termux-reload-settings)r    r   r   )Zpatchr   r   r   r	   �huhu$   s    r!   c              C   s�   t �  xZdD ]R} x>td�D ]2}ttt�ttjtj � d ddd� td� qW t| ddd� qW t �  t	�
dtt�� d	�� d S )
Nz
loading...r   �� T)r   �flushg{�G�z�?zecho -e -n "z""; cowsay -f skeleton termux-style)r
   r   r   r   r   �stZascii_lettersZdigitsr   r   r   )r   �nr   r   r	   �hed(   s    
&r'   c           
   C   s�   y8t ttt�� dtd�� dtd�� dtt�� d���} W n   t�  Y nX | dkr\t�  n&| dkrlt�  n| d	kr|t�  nt�  d S )
Nzfont: zfont.txtz
color: z	color.txt�
z 1. Font
2. Tema
3. Contact me
# r   �   �   )	�int�inputr   r   r   r   �font�color�contact)Zwhutr   r   r	   �nanya2   s    8r0   c              C   s>  d} d}t �|�}x0|D ](}ttd t| � d | � | d7 } qW d} y(|tttt�d tt� ��d  }W n   t�  Y nX t �|| �}x8|D ]0}ttd t| � d |�	dd� � | d7 } q�W y(|tttt�d tt� ��d  }W n   t�  Y nX || d | }t
d	d
��|�	dd�� t|d� d S )Nr   zfonts/r   z. zPilih: z.ttfr#   �/zfont.txtr   zfont.ttf)r   r   r   r   �strr+   r,   r   r   �replacer   �writer!   )r   �patr   r   �mnaZyekZsni�uwur   r   r	   r-   @   s,    

(
$(r-   c              C   s�   d} d}t �|�}x8|D ]0}ttd t| � d |�dd� � | d7 } qW y(|tttt�d tt� ��d  }W n   t	�  Y nX || }t
dd	��|�dd�� t|d
� d S )Nr   zcolors/r   z. z.colorsr#   zPilih: z	color.txtr   zcolors.properties)r   r   r   r   r2   r3   r+   r,   r   r   r   r4   r!   )r   r5   r   r   r6   r7   r   r   r	   r.   X   s    

$(r.   c              C   sj   y$t ttt�� dtt�� d���} W n   t�  Y nX | dkrLt�d� n| dkr`t�d� nt�  d S )Nz1. WA
2. FB
z# r   z%xdg-open https://wa.me/62895640466851r)   z(xdg-open https://fb.me/mayat.mayat.58555)r+   r,   r   r   r   r   r   )r7   r   r   r	   r/   g   s    $r/   )r   �stringr%   �sysZrandomr   r   Ztimer   r   r   r
   r   r   r    r!   r'   r0   r-   r.   r/   r   r   r   r	   �<module>   s"   

