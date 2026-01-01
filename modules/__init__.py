"""Dataset Augmentation Tool Modules"""
from .paraphrase_generator import ParaphraseGenerator
from .synonym_replacer import SynonymReplacer
from .back_translator import BackTranslator
from .noise_injector import NoiseInjector
from .style_transformer import StyleTransformer
from .entity_swapper import EntitySwapper
from .context_expander import ContextExpander
from .label_preserver import LabelPreserver
from .quality_checker import QualityChecker
from .batch_processor import BatchProcessor
__all__ = ['ParaphraseGenerator', 'SynonymReplacer', 'BackTranslator', 'NoiseInjector', 'StyleTransformer',
           'EntitySwapper', 'ContextExpander', 'LabelPreserver', 'QualityChecker', 'BatchProcessor']
