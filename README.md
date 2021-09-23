# WordSearchPuzzle

This program generates a word search puzzle board with random words found on the web.
In case the automatic web search for words fails for any reason, a backup pool of words (**backupwords.txt**) will be used instead.

This game supports words printed in 4 directions:
	top to bottom
	bottom to top
	left to right
	right to left

The size of the board is hardcoded 15x15 (but I could be customized if needed, directly in the source code, by changing the variable '**bsize = 15**')

Output example:

**How many words would you like to search in the puzzle? [min 1, max 10]**:

&gt;&gt; 8

**Words to look for**:
<br />SEGNITY
<br />REFUGIUM
<br />QUAGGA
<br />NEMBUTSU
<br />MUSROL
<br />QUONDAM


<br />R  G  N  M  Z  O  M  Z  Q  F  U  W  M  R  H
<br />A  Y  V  H  B  W  H  Y  Z  P  C  L  Y  S  U
<br />Q  U  J  T  O  F  S  M  U  I  G  U  F  E  R
<br />B  I  O  W  U  M  Q  U  G  M  C  Y  A  A  D
<br />J  Z  E  Z  F  Z  S  S  T  U  H  S  R  D  Q
<br />A  C  X  W  Y  K  A  U  X  T  Q  M  X  N  K
<br />L  C  S  U  U  K  E  P  J  E  O  M  W  J  L
<br />K  U  E  R  E  W  P  F  C  G  H  A  B  B  G
<br />G  Z  G  L  N  Z  J  Y  H  M  A  D  R  I  Z
<br />V  L  N  Q  U  A  G  G  A  V  O  N  Z  N  J
<br />X  O  I  H  G  R  O  D  D  S  S  O  X  X  Y
<br />P  R  T  A  P  X  A  L  N  E  K  U  L  Y  H
<br />T  S  Y  B  P  E  Y  Q  D  V  V  Q  X  D  R
<br />N  U  K  U  N  E  M  B  U  T  S  U  W  E  O
<br />Z  M  V  F  G  W  D  S  Z  O  U  D  B  M  I

