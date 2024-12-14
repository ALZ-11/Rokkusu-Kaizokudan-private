# Application de Chat Multi-Documents Gemini  

L’application de Chat Multi-Documents Gemini est un outil avancé permettant d’interagir avec et de questionner plusieurs documents textuels. En exploitant les capacités des modèles Gemini de Google Generative AI, cette application facilite les conversations contextuelles, simplifiant ainsi la recherche d’informations et l’analyse documentaire. Les utilisateurs peuvent téléverser jusqu’à quatre fichiers texte et poser des questions en langage naturel via une interface de chat intuitive.  

Cette application intègre les modèles Gemini de Google Generative AI, tels que Gemini Pro, Pro Vision et Ultra, offrant des options adaptées à divers besoins. Une fois les documents téléversés, ils sont segmentés en indices vectoriels à l’aide de LlamaIndex, une plateforme performante pour la gestion et la recherche de données textuelles. Le moteur de chat intégré exploite des algorithmes de similarité sémantique et des techniques avancées d’inférence pour fournir des réponses pertinentes et exploitables.  

L’interface conviviale de Streamlit permet des interactions fluides. La barre latérale offre des options pour téléverser des fichiers, configurer les paramètres du modèle IA et réinitialiser les conversations. Les utilisateurs peuvent ajuster dynamiquement des paramètres comme la créativité des réponses (température) et sélectionner parmi les modèles Gemini disponibles. Cette flexibilité garantit que l’application peut répondre aussi bien à des requêtes simples qu’à des besoins analytiques complexes, tout en offrant une expérience utilisateur optimisée.  

Sur le plan technique, l’application repose sur des frameworks et bibliothèques modernes. Construite avec Streamlit pour son interface interactive, elle utilise le SDK de Google Generative AI pour interagir avec les modèles Gemini, ainsi que LlamaIndex pour segmenter et indexer les documents. Les documents sont découpés en segments de taille gérable (par défaut : 512 tokens avec un chevauchement de 50 tokens) pour optimiser les processus d’intégration et de requête. Ces intégrations sont générées grâce aux modèles d’intégration stables et performants de Gemini, garantissant des réponses rapides et précises. Les activités de l’application et les erreurs sont enregistrées à l’aide d’un système de journalisation intégré, facilitant le débogage et le suivi des performances.  

Pour commencer, clonez le dépôt et installez les dépendances nécessaires avec la commande suivante :  
```bash
pip install -r requirements.txt


Voici le fichier README rédigé en français, présenté au format Markdown :

markdown
Copy code
# Application de Chat Multi-Documents Gemini  

L’application de Chat Multi-Documents Gemini est un outil avancé permettant d’interagir avec et de questionner plusieurs documents textuels. En exploitant les capacités des modèles Gemini de Google Generative AI, cette application facilite les conversations contextuelles, simplifiant ainsi la recherche d’informations et l’analyse documentaire. Les utilisateurs peuvent téléverser jusqu’à quatre fichiers texte et poser des questions en langage naturel via une interface de chat intuitive.  

Cette application intègre les modèles Gemini de Google Generative AI, tels que Gemini Pro, Pro Vision et Ultra, offrant des options adaptées à divers besoins. Une fois les documents téléversés, ils sont segmentés en indices vectoriels à l’aide de LlamaIndex, une plateforme performante pour la gestion et la recherche de données textuelles. Le moteur de chat intégré exploite des algorithmes de similarité sémantique et des techniques avancées d’inférence pour fournir des réponses pertinentes et exploitables.  

L’interface conviviale de Streamlit permet des interactions fluides. La barre latérale offre des options pour téléverser des fichiers, configurer les paramètres du modèle IA et réinitialiser les conversations. Les utilisateurs peuvent ajuster dynamiquement des paramètres comme la créativité des réponses (température) et sélectionner parmi les modèles Gemini disponibles. Cette flexibilité garantit que l’application peut répondre aussi bien à des requêtes simples qu’à des besoins analytiques complexes, tout en offrant une expérience utilisateur optimisée.  

Sur le plan technique, l’application repose sur des frameworks et bibliothèques modernes. Construite avec Streamlit pour son interface interactive, elle utilise le SDK de Google Generative AI pour interagir avec les modèles Gemini, ainsi que LlamaIndex pour segmenter et indexer les documents. Les documents sont découpés en segments de taille gérable (par défaut : 512 tokens avec un chevauchement de 50 tokens) pour optimiser les processus d’intégration et de requête. Ces intégrations sont générées grâce aux modèles d’intégration stables et performants de Gemini, garantissant des réponses rapides et précises. Les activités de l’application et les erreurs sont enregistrées à l’aide d’un système de journalisation intégré, facilitant le débogage et le suivi des performances.  

Pour commencer, clonez le dépôt et installez les dépendances nécessaires avec la commande suivante :  
```bash
pip install -r requirements.txt
Configurez ensuite votre clé API Google Generative AI directement dans le script, puis lancez l’application avec :

bash
Copy code
streamlit run rag_multi_gemini.py
L’interface de l’application permet de téléverser des documents texte, d’ajuster les paramètres et de démarrer des requêtes dans un environnement de chat intuitif.

L’application est configurée avec des paramètres par défaut définis dans la classe AppConfig. Ces paramètres incluent une limite de tokens de 1024 par réponse, un niveau de créativité fixé à 0,3 et un fichier de journalisation nommé app.log pour suivre les activités. Les utilisateurs peuvent personnaliser davantage ces paramètres pour les adapter à leurs besoins spécifiques.
