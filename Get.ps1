$courses = ".\Cources.txt"
$coursesOut = ".\courses-done.txt"

$urls = get-content $courses
if ($urls.GetType() -ne [System.String]) {
    [System.Collections.ArrayList]$urlsOut = $urls
} else {
    $urlsOut = ""
}

if ($username -eq $null) {
    $username = read-host -promt "User"
}

if ($password -eq $null) {
    $password = read-host -promt "Passwrd"
}

$cmdPath = "youtube-dl.exe"

for ($i=0; $i -le 4; $i++) {
    if ($urls.Count -eq 1) {
        $cmdArgList = @(
            "--username", $username,
            "--password", $password,
            "--verbose",
            "--sleep-interval", 120,
            "-o", "%(playlist_title)s\%(playlist_index)s-%(title)s.%(ext)s",
            $urls
        ) 

        & $cmdPath $cmdArgList

        $urls | Out-File -FilePath $coursesOut -Append

        break

    } elseif ($i -le $urls.Count) {
        $cmdArgList = @(
            "--username", $username,
            "--password", $password,
            "--verbose",
            "--sleep-interval", 120,
            "-o", "%(playlist_title)s\%(playlist_index)s-%(title)s.%(ext)s",
            $urls[$i]
        ) 

        & $cmdPath $cmdArgList

        $urlsOut.remove($urls[$i])

        $urls[$i] | Out-File -FilePath $coursesOut -Append
        
    } 
}

$urlsOut | Out-File -FilePath $courses