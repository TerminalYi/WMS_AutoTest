import yaml


class YamlUtil:

    @classmethod
    def get_yaml(cls, yaml_path):
        with open(yaml_path, "r", encoding='utf-8') as f:
            return yaml.safe_load(f).values()

