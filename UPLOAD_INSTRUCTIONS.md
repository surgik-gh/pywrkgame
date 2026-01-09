# Инструкции по загрузке PyWRKGame 3.0.0 на PyPI

## Статус

✅ **Пакет готов**: `dist/pywrkgame-3.0.0.tar.gz` (1.1 MB)
✅ **Проверка пройдена**: `twine check` - PASSED
✅ **Все тесты пройдены**: Python (10 passed, 3 skipped), C++ (156 passed, 4 skipped)
✅ **Test PyPI работает**: Соединение с test.pypi.org успешно
✅ **GitHub Actions готов**: Workflow для автоматической загрузки создан
❌ **Production PyPI**: SSL/сетевая ошибка при подключении с локальной машины

## РЕКОМЕНДУЕМОЕ РЕШЕНИЕ: GitHub Actions

Создан workflow `.github/workflows/publish-pypi.yml` для автоматической загрузки через GitHub.

### Шаги:

#### 1. Закоммитьте и запушьте изменения

```bash
git add .
git commit -m "Add PyPI publishing workflow"
git push origin main
```

#### 2. Добавьте API токен в GitHub Secrets

1. Откройте ваш репозиторий на GitHub
2. Перейдите: **Settings** → **Secrets and variables** → **Actions**
3. Нажмите **New repository secret**
4. Имя: `PYPI_API_TOKEN`
5. Значение: `<ваш PyPI API токен>`
6. Нажмите **Add secret**

#### 3. Запустите workflow

1. Перейдите: **Actions** → **Publish to PyPI**
2. Нажмите **Run workflow**
3. В поле "Type 'publish' to confirm" введите: `publish`
4. Нажмите **Run workflow**

#### 4. Дождитесь завершения

Workflow автоматически:
- Соберет пакет
- Проверит его
- Загрузит на PyPI
- Покажет ссылку на пакет

#### 5. Проверьте публикацию

После успешного выполнения:
- Откройте: https://pypi.org/project/pywrkgame/
- Установите: `pip install pywrkgame`

## Альтернативные решения

### Вариант 1: Используйте другой компьютер/сервер

Если у вас есть доступ к Linux/macOS машине или серверу:

```bash
# Скопируйте файл на другую машину
scp dist/pywrkgame-3.0.0.tar.gz user@server:~/

# На другой машине:
pip install twine
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<ваш PyPI API токен>
twine upload pywrkgame-3.0.0.tar.gz
```

### Вариант 2: Установите WSL и загрузите оттуда

```bash
# Установите WSL (в PowerShell от администратора):
wsl --install

# После перезагрузки, в WSL:
cd /mnt/d/projects/lib/pyworkergame
pip install twine
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<ваш PyPI API токен>
twine upload dist/pywrkgame-3.0.0.tar.gz
```

### Вариант 3: Проверьте сетевые настройки

Проблема может быть в:
- **Антивирус/Файрвол**: Временно отключите и попробуйте снова
- **Корпоративная сеть**: Попробуйте с другого интернет-подключения
- **VPN**: Попробуйте с VPN или без него

После изменений:
```powershell
$env:TWINE_USERNAME="__token__"
$env:TWINE_PASSWORD="<ваш PyPI API токен>"
twine upload dist/pywrkgame-3.0.0.tar.gz
```

## Информация о пакете

- **Имя**: pywrkgame
- **Версия**: 3.0.0
- **Файл**: dist/pywrkgame-3.0.0.tar.gz
- **Размер**: 1,107,776 байт (1.1 MB)
- **Тип**: Source Distribution (sdist)
- **Путь**: `D:\projects\lib\pyworkergame\dist\pywrkgame-3.0.0.tar.gz`

## Диагностика

**Что работает:**
- ✓ Сборка пакета
- ✓ Проверка пакета (twine check)
- ✓ Соединение с test.pypi.org
- ✓ Все тесты

**Что не работает:**
- ✗ Соединение с upload.pypi.org с локальной Windows машины

**Причина:** SSL/сетевая проблема специфичная для upload.pypi.org в вашей сети.

**Решение:** Использовать GitHub Actions (Linux окружение) для загрузки.

## После успешной загрузки

1. Проверьте страницу: https://pypi.org/project/pywrkgame/
2. Установите: `pip install pywrkgame`
3. Проверьте: `python -c "import pywrkgame; print('Success!')"`

## Технические детали

- **SystemManager исправлен**: Добавлены `delete` для конструктора копирования
- **setup.py обновлен**: Все необходимые исходные файлы включены
- **Wheel не собран**: Требуются внешние зависимости (GLM, Box2D, Bullet3)
- **Source distribution достаточен**: Пользователи смогут собрать локально

## Поддержка

- PyPI Support: https://pypi.org/help/
- GitHub Actions Docs: https://docs.github.com/en/actions
- Twine Documentation: https://twine.readthedocs.io/
