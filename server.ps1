$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:8080/")
$listener.Start()
Write-Output "Server running on http://localhost:8080"
while ($listener.IsListening) {
    $context = $listener.GetContext()
    $response = $context.Response
    $request = $context.Request
    
    $localPath = "c:\Users\User\Downloads\SEO-20260506T052936Z-3-001\SEO\web4" + $request.Url.LocalPath.Replace("/", "\")
    if ($localPath.EndsWith("\")) { $localPath += "index.html" }
    
    if (Test-Path $localPath) {
        $content = [System.IO.File]::ReadAllBytes($localPath)
        $response.ContentLength64 = $content.Length
        if ($localPath.EndsWith(".css")) { $response.ContentType = "text/css" }
        elseif ($localPath.EndsWith(".js")) { $response.ContentType = "application/javascript" }
        elseif ($localPath.EndsWith(".png")) { $response.ContentType = "image/png" }
        elseif ($localPath.EndsWith(".html")) { $response.ContentType = "text/html" }
        
        $response.OutputStream.Write($content, 0, $content.Length)
    } else {
        $response.StatusCode = 404
    }
    $response.Close()
}
