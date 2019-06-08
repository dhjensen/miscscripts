function Test-XMLFile {
    <#
        .SYNOPSIS
        Test the validity of an XML file
    #>
    [CmdletBinding()]
    param (
        [parameter(mandatory=$true)][ValidateNotNullorEmpty()][string]$xmlFilePath
    )

    # Check the file exists
    if (!(Test-Path -Path $xmlFilePath)){
        throw "$xmlFilePath is not valid. Please provide a valid path to the .xml file"
    }
    #Write-Host $xmlFilePath

    # Check for Load or Parse errors when loading the XML file
    $xml = New-Object System.Xml.XmlDocument
    try {
        $xml.Load((Get-ChildItem -Path $xmlFilePath).FullName)
        #return $true
    }
    catch [System.Xml.XmlException] {
        Write-Verbose "$xmlFilePath : $($_.toString())"
        #return $false
    }
}

$pa = "C:\ProgramData\chocolatey"
$exclude = @("*.arguments", "*.exe*", "*.txt", "*.dll", "*.cmd", "*.log", "*.msi*", "*.nupkg", "*.ps1", "*.chm", "*.hlm", "*.CNT", "*.SYS", "*.jpg", "*.HLP", "*.PSM1", "*.png")

Get-ChildItem -Recurse -Exclude $exclude -file -Path $pa | ForEach-Object {
    Test-XMLFile $_.FullName -Verbose
}
