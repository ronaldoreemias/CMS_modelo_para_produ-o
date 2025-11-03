document.addEventListener('DOMContentLoaded', function() {
            const languageSelect = document.getElementById('languageSelect');
            
            // Verificar se há um idioma salvo no localStorage
            const savedLanguage = localStorage.getItem('selectedLanguage');
            if (savedLanguage) {
                languageSelect.value = savedLanguage;
                setLanguage(savedLanguage);
            }
            
            // Adicionar evento de mudança ao seletor de idioma
            languageSelect.addEventListener('change', function() {
                const selectedLanguage = this.value;
                setLanguage(selectedLanguage);
                
                // Salvar a preferência no localStorage
                localStorage.setItem('selectedLanguage', selectedLanguage);
            });
            
            function setLanguage(lang) {
                // Atualizar todos os elementos com atributos de dados
                const elements = document.querySelectorAll('[data-pt], [data-en], [data-es]');
                
                elements.forEach(element => {
                    if (element.hasAttribute(`data-${lang}`)) {
                        // Verificar se é um input ou textarea
                        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                            element.value = element.getAttribute(`data-${lang}`);
                        } else {
                            element.textContent = element.getAttribute(`data-${lang}`);
                        }
                    }
                });
                
                // Atualizar o atributo lang do HTML
                document.documentElement.setAttribute('lang', lang);
            }
        });