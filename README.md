
## Azure CLIをセットアップする

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## Azure CLIでログインする

```bash
az login --tenant $AZURE_TENANT_ID
```

## 動作確認

```bash
az version
az account list
```
