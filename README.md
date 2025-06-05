# 🧪 Simulado Técnico – Desenvolvedor RPA Python com Testes Automatizados

## 🎯 Objetivo
Automatizar e testar um processo de login utilizando Selenium WebDriver com Python, estruturando o projeto com boas práticas e simulação de um pipeline CI/CD.

---

## ✅ Parte 1: Automação com Selenium

### Cenário:
Automatize o seguinte fluxo no site: [https://www.saucedemo.com](https://www.saucedemo.com)

**Fluxo:**
- Acessar a página de login
- Preencher usuário: `standard_user`
- Preencher senha: `secret_sauce`
- Clicar em login
- Validar que foi redirecionado para a página de produtos (`/inventory`)
- Capturar um screenshot da tela final
- Gerar um log de sucesso ou erro

**Dicas:**
- Use `WebDriverWait` para esperar elementos carregarem
- Use `logging` para registrar o resultado do processo

---

## ✅ Parte 2: Teste Automatizado com PyTest

### Instruções:
- Criar testes com `pytest` validando o login
- Usar `try-except` para capturar falhas
- Se ocorrer erro:
  - Gerar log com erro
  - Capturar screenshot com timestamp

**Exemplo básico:**
```python
def test_login_success():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    driver.quit()
