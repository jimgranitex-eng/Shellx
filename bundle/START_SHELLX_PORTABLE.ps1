param(
    [ValidateSet('doctor','launcher','preflight','daemon-once','brain','bridge')]
    [string]$Mode = 'doctor'
)

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

if (Get-Command py -ErrorAction SilentlyContinue) {
    $PythonCmd = 'py -3'
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $PythonCmd = 'python'
} else {
    throw 'Python was not found on PATH.'
}

switch ($Mode) {
    'doctor' {
        Invoke-Expression "$PythonCmd .\core\ai_heart_doctor.py"
    }
    'launcher' {
        Invoke-Expression "$PythonCmd .\core\ai_heart_launcher.py"
    }
    'preflight' {
        Invoke-Expression "$PythonCmd -c \"from core.ai_heart_system_utils import preflight_check; ok, issues = preflight_check(); print('PREFLIGHT_OK=', ok); print('\\n'.join(issues) if issues else 'NO_ISSUES')\""
    }
    'daemon-once' {
        Invoke-Expression "$PythonCmd .\core\ai_heart_daemon.py --once"
    }
    'brain' {
        Invoke-Expression "$PythonCmd .\core\ai_brain.py"
    }
    'bridge' {
        Invoke-Expression "$PythonCmd .\bridge\grok_http_bridge.py"
    }
}
