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
        throw "$xmlFilePath does not exist. Please provide a valid path to the .xml file"
    }

    # Check for Load or Parse errors when loading the XML file
    $xml = New-Object System.Xml.XmlDocument
    try {
        $xml.Load((Get-ChildItem -Path $xmlFilePath).FullName)
        return ($true).ToString()
    }
    catch [System.Xml.XmlException] {
        Write-Verbose "$xmlFilePath : $($_.toString())"
        return $_.toString()
    }
}

$ChocoInstallDir = "C:\ProgramData\chocolatey"

# XML file extensions that choco use
$include = @("*.config", "*.files", "*.registry")

# Get all files including hidden ones that match include list
Get-ChildItem -Recurse -include $include -Path $ChocoInstallDir -Force -File | ForEach-Object {
    #Test-XMLFile $_.FullName -Verbose
    [PSCustomObject]@{
        FullPath = $_.FullName
        ValidXML = Test-XMLFile $_.FullName
    }
}