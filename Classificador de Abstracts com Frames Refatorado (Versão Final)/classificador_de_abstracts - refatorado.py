# -*- coding: UTF-8 -*-
import os
import uuid
import json
import hashlib
import xml.etree.cElementTree as ET
import re
from textwrap import fill
from textwrap import shorten
import csv

abstracts = [
    "----------------------------- Agronomy ------------------------------",
    "01 - Bioenergy and climate change mitigation: an assessment",
    "02 - Mineral-Organic Associations: Formation, Properties, and Relevance in Soil Environments",
    "03 - Eight principles of integrated pest management",
    "04 - Climate forcing datasets for agricultural modeling: Merged products for gap-filling and historical climate series estimation",
    "05 - Genome-wide association study for grain yield and related traits in an elite spring wheat population grown in temperate irrigated environments",
    "----------------------------- Business -------------------------------",
    "06 - The Microfoundations Movement in Strategy and Organization Theory",
    "07 - Event System Theory: An Event-Oriented Approach To The Organizational  Sciences",
    "08 - A new criterion for assessing discriminant validity in variance-based structural equation modeling",
    "09 - Virtual Teams Research: 10 Years, 10 Themes, and 10 Opportunities",
    "10 - Understanding Customer Experience Throughout the Customer Journey",
    "----------------------------- Chemistry ------------------------------",
    "11 - Graphitic Carbon Nitride (g-C3N4)-Based Photocatalysts for Artificial Photosynthesis and Environmental Remediation: Are We a Step Closer To   Achieving Sustainability?",
    "12 - Noble metal-free hydrogen evolution catalysts for water splitting",
    "13 - Cesium-containing triple cation perovskite solar cells: improved    stability, reproducibility and high efficiency",
    "14 - Towards greener and more sustainable batteries for electrical energy  storage",
    "15 - Free Polymer Solar Cells with over 11% Efficiency and Excellent Thermal Stability",
    "----------------------- Cognitive Linguistics ------------------------",
    "16 - Moving beyond 'Next Wednesday': The interplay of lexical semantics and  constructional meaning in an ambiguous metaphoric statement",
    "17 - Visualizing onomasiological change: Diachronic variation in metonymic patterns for WOMAN in Chinese",
    "18 - Cognitive Grammar and gesture: Points of convergence, advances and challenges",
    "19 - Constructional meaning representation within a knowledge engineering framework",
    "20 - Operationalizing mirativity A usage-based quantitative study of constructional construal in English",
    "-------------------------- Computer Science --------------------------",
    "21 - Fitting Linear Mixed-Effects Models Using lme4",
    "22 - Deep Convolutional Neural Networks for Computer-Aided Detection: CNN   Architectures, Dataset Characteristics and Transfer Learning",
    "23 - Structural Damage Detection Using Modal Strain Energy and Hybrid  Multiobjective Optimization",
    "24 - A Survey on Demand Response in Smart Grids: Mathematical Models and Approaches",
    "25 - Trainable COSFIRE filters for vessel delineation with application to retinal images",
    "----------------------------- Engineering ----------------------------",
    "26 - Free vibration analysis of nonlocal strain gradient beams made of functionally graded material",
    "27 - Topology Optimization in Aircraft and Aerospace Structures Design",
    "28 - Mechanical and tribological properties of self-lubricating metal matrix nanocomposites reinforced by carbon nanotubes (CNTs) and graphene – A review",
    "29 - A comprehensive experimental and modeling study of isobutene oxidation",
    "30 - Nanofluid flow and heat transfer between parallel plates considering  Brownian motion using DTM",
    "------------------- Health Care Sciences and Services ----------------",
    "31 - Coproduction of healthcare service",
    "32 - The Mass Production of Redundant, Misleading, and Conflicted Systematic   Reviews and Meta-analyses",
    "33 - Cost-Effectiveness Analysis Alongside Clinical Trials II-An ISPOR Good    Research Practices Task Force Report",
    "34 - Food Insecurity And Health Outcomes",
    "35 - The Effect of an Intervention to Break the Gender Bias Habit for Faculty   at One Institution: A Cluster Randomized, Controlled Trial",
    "----------------------------- Linguistics ----------------------------",
    "36 - Identity and a Model of Investment in Applied Linguistics",
    "37 - Academic publishing and the myth of linguistic injustice",
    "38 - The Effectiveness of L2 Pronunciation Instruction: A Narrative Review",
    "39 - Fast oscillatory dynamics during language comprehension: Unification    versus maintenance and prediction?",
    "40 - Statistical learning as an individual ability: Theoretical perspectives and empirical evidence",
    "------------------------------- Physics ------------------------------",
    "41 - Spin Hall effects",
    "42 - Magnon spintronics",
    "43 - Reactive species in non-equilibrium atmospheric-pressure plasmas:  Generation, transport, and biological effects",
    "44 - Experimental Discovery of Weyl Semimetal TaAs",
    "45 - Physics of microswimmers-single particle motion and collective behavior:    a review",
    "------------------------ Telecommunications --------------------------",
    "46 - Internet of Things: A Survey on Enabling Technologies, Protocols, and    Applications",
    "47 - Non-Orthogonal Multiple Access for 5G: Solutions, Challenges, Opportunities, and Future Research Trends",
    "48 - LTE-UNLICENSED: THE FUTURE OF SPECTRUM AGGREGATION FOR CELLULAR NETWORKS",
    "49 - System Architecture and Key Technologies for 5G Heterogeneous Cloud  Radio Access Networks",
    "50 - Cooperative Non-orthogonal Multiple Access With Simultaneous Wireless Information and Power Transfer"
]
contador = 0;
abstractsTagged = [
    {"title": "01 - Bioenergy and climate change mitigation: an assessment",
     "content": {
        "abstract": "<topic> Bioenergy deployment </topic> <gap> offers significant potential for climate change mitigation, but also carries considerable risks. </gap> <goal> In this review, we bring together perspectives of various communities involved in the research and regulation of bioenergy deployment in the context of climate change mitigation: Land-use and energy experts, land-use and integrated assessment modelers, human geographers, ecosystem researchers, climate scientists and two different strands of life-cycle assessment experts. </goal> <method> We summarize technological options, outline the state-of-the-art knowledge on various climate effects, provide an update on estimates of technical resource potential and comprehensively identify sustainability effects. Cellulosic feedstocks, increased end-use efficiency, improved land carbon-stock management and residue use, and, when fully developed, BECCS appear as the most promising options, depending on development costs, implementation, learning, and risk management. Combined heat and power, efficient biomass cookstoves and small-scale power generation for rural areas can help to promote energy access and sustainable development, along with reduced emissions. We estimate the sustainable technical potential as up to 100EJ: high agreement; 100-300EJ: medium agreement; above 300EJ: low agreement. Stabilization scenarios indicate that bioenergy may supply from 10 to 245EJyr(-1) to global primary energy supply by 2050. Models indicate that, if technological and governance preconditions are met, large-scale deployment (>200EJ), together with BECCS, could help to keep global warming below 2 degrees degrees of preindustrial levels; but such high deployment of land-intensive bioenergy feedstocks could also lead to detrimental climate effects, negatively impact ecosystems, biodiversity and livelihoods. The integration of bioenergy systems into agriculture and forest landscapes can improve land and water use efficiency and help address concerns about environmental impacts. </method> <conclusion> We conclude that the high variability in pathways, uncertainties in technological development and ambiguity in political decision render forecasts on deployment levels and climate effects very difficult. However, uncertainty about projections should not preclude pursuing beneficial bioenergy options. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Agronomy]"
    }
    },
    {"title": "02 - Mineral-Organic Associations: Formation, Properties, and Relevance in Soil Environments",
     "content": {
         "abstract": "<topic> Minerals and organic matter (OM) may form intricate associations </topic> <gap> via myriad interactions. In soils, the associations of OM with mineral surfaces are mainly investigated because of their role in determining the long-term retention of OM. OM \"must decay in order to release the energy and nutrients that drive live processes all over the planet\" (Janzen, 2006). Thus, the processes and mechanisms that retain OM in soil are a central concern to very different branches of environmental research. An agronomist may want to synchronize periods of high nutrient and energy release with the growth stages of a crop. An environmental chemist may wish to either immobilize an organic soil contaminant or enhance its decomposition into less harmful metabolites, while climate scientists need to understand the processes that mediate the production of potent greenhouse gases from decomposing OM. Associations of OM with pedogenic minerals (henceforth termed mineral-organic associations (MOAs)) are known to be key controls in these and many other processes. </gap> <goal> Here we strive to present an overview of the current knowledge on MOAs and identify key questions and future research needs. </goal>",
         "macrostructure": "<topic> \n <gap> \n <goal>",
         "type": "[Agronomy]"
     }
    },
    {"title": "03 - Eight principles of integrated pest management",
     "content": {
         "abstract": "<gap> The use of pesticides made it possible to increase yields, simplify cropping systems, and forego more complicated crop protection strategies. Over-reliance on chemical control, however, is associated with contamination of ecosystems and undesirable health effects. The future of crop production is now also threatened by emergence of pest resistance and declining availability of active substances. There is therefore a need to design cropping systems less dependent on synthetic pesticides. Consequently, the European Union requires the application of <topic> eight principles (P) of Integrated Pest Management </topic> that fit within sustainable farm management. </gap> <goal> Here, we propose to farmers, advisors, and researchers a dynamic and flexible approach that accounts for the diversity of farming situations and the complexities of agroecosystems and that can improve the resilience of cropping systems and our capacity to adapt crop protection to local realities. </goal> <method> For each principle (P), we suggest that (P1) the design of inherently robust cropping systems using a combination of agronomic levers is key to prevention. (P2) Local availability of monitoring, warning, and forecasting systems is a reality to contend with. (P3) The decision-making process can integrate cropping system factors to develop longer-term strategies. (P4) The combination of non-chemical methods that may be individually less efficient than pesticides can generate valuable synergies. (P5) Development of new biological agents and products and the use of existing databases offer options for the selection of products minimizing impact on health, the environment, and biological regulation of pests. (P6) Reduced pesticide use can be effectively combined with other tactics. (P7) Addressing the root causes of pesticide resistance is the best way to find sustainable crop protection solutions. And (P8) integration of multi-season effects and trade-offs in evaluation criteria will help develop sustainable solutions. </method>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method>",
         "type": "[Agronomy]"
     }
    },
    {"title": "04 - Climate forcing datasets for agricultural modeling: Merged products for gap-filling and historical climate series estimation",
     "content": {
        "abstract": "<gap> The AgMERRA and AgCFSR <topic> climate forcing datasets </topic> provide daily, high-resolution, continuous, meteorological series over the 1980-2010 period designed for applications examining the agricultural impacts of climate variability and climate change. </gap> <method> These datasets combine daily resolution data from retrospective analyses (the Modern-Era Retrospective Analysis for Research and Applications, MERRA, and the Climate Forecast System Reanalysis, CFSR) with in situ and remotely-sensed observational datasets for temperature, precipitation, and solar radiation, leading to substantial reductions in bias in comparison to a network of 2324 agricultural-region stations from the Hadley Integrated Surface Dataset (HadISD). </method> <conclusion> Results compare favorably against the original reanalyses as well as the leading climate forcing datasets (Princeton, WFD, WFD-EI, and GRASP), and AgMERRA distinguishes itself with substantially improved representation of daily precipitation distributions and extreme events owing to its use of the MERRA-Land dataset. These datasets also peg relative humidity to the maximum temperature time of day, allowing for more accurate representation of the diurnal cycle of near-surface moisture in agricultural models. AgMERRA and AgCFSR enable a number of ongoing investigations in the Agricultural Model Intercomparison and Improvement Project (AgMIP) and related research networks, and may be used to fill gaps in historical observations as well as a basis for the generation of future climate scenarios. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion>",
        "type": "[Agronomy]"
     }
    },
    {"title": "05 - Genome-wide association study for grain yield and related traits in an elite spring wheat population grown in temperate irrigated environments",
     "content": {
        "abstract": "<topic> Through genome-wide association study, </topic> <method> loci for grain yield and yield components were identified in chromosomes 5A and 6A in spring wheat (Triticum aestivum). Genome-wide association study (GWAS) was conducted for grain yield (YLD) and yield components on a wheat association mapping initiative (WAMI) population of 287 elite, spring wheat lines grown under temperate irrigated high-yield potential condition in Ciudad Obregn, Mexico, during four crop cycles (from 2009-2010 to 2012-2013). The population was genotyped with high-density Illumina iSelect 90K single nucleotide polymorphisms (SNPs) assay. </method> <conclusion> An analysis of traits across subpopulations indicated that lines with 1B/1R translocation had higher YLD, grain weight, and taller plants than lines without the translocation. GWAS using 18,704 SNPs identified 31 loci that explained 5-14 % of the variation in individual traits. We identified SNPs in chromosome 5A and 6A that were significantly associated with yield and yield components. Four loci were detected for YLD in chromosomes 3B, 5A, 5B, and 6A and the locus in 5A explained 5 % of the variation for grain number/m(2). The locus for YLD in chromosome 6A also explained 6 % of the variation in grain weight. Loci significantly associated with maturity were identified in chromosomes 2B, 3B, 4B, 4D, and 6A and for plant height in 1A and 6A. Loci were also detected for canopy temperature at grain filling (2D, 4D, 6A), chlorophyll index at grain filling (3B and 6A), biomass (3D and 6A) and harvest index (1D, 1B, and 3B) that explained 5-10 % variation. These markers will be further validated. </conclusion>",
        "macrostructure": "<topic> \n <method> \n <conclusion>",
        "type": "[Agronomy]"
    }
    },
    {"title": "06 - The Microfoundations Movement in Strategy and Organization Theory",
     "content": {
         "abstract": "<topic> Microfoundations </topic> <gap> have received increased attention in strategy and organization theory over the past decade. <goal> In this paper, we take stock of the microfoundations movement, its origins and history, and disparate forms. We briefly touch on similar micro movements in disciplines such as economics and sociology. </gap> However, our particular focus is on the unique features of the microfoundations movement in macro management. <method> While the microfoundations movement in macro management does seek to link with more micro disciplines such as psychology and organizational behavior, it also features a unique set of questions, assumptions, theoretical mechanisms, and independent/dependent variables that complement the focus in the micro disciplines. We also discuss the disparate criticisms of the microfoundations literature and the challenges the movement faces, such as defining distinct theoretical and empirical programs for microfoundational research. </method> The overall purpose of this manuscript is to clearly delineate the promise and uniqueness of microfoundations research in macro management, to discuss how the movement originated and where it is going, and to offer rich opportunities for future work. </goal>",
         "macrostructure": "<topic> \n <gap> \n <goal> \n <gap> \n <goal> \n <method> \n <goal>",
         "type": "[Business]"
     }
    },
    {"title": "07 - Event System Theory: An Event-Oriented Approach To The Organizational  Sciences",
     "content": {
         "abstract": "<topic> Organizations are dynamic, hierarchically structured entities. </topic> <gap> Such dynamism is reflected in the emergence of significant events at every organizational level. Despite this fact, there has been relatively little discussion about how events become meaningful and come to impact organizations across space and time. </gap> <method> We address this gap by developing event system theory, which suggests that events become salient when they are novel, disruptive, and critical (reflecting an event's strength). Importantly, events can originate at any hierarchical level and their effects can remain within that level or travel up or down throughout the organization, changing or creating new behaviors, features, and events. </method> <conclusion> This impact can extend over time as events vary in duration and timing or as event strength evolves. Event system theory provides a needed shift in focus for organizational theory and research by developing specific propositions articulating the interplay among event strength and the spatial and temporal processes through which events come to influence organizations. </conclusion>",
         "macrostructure": "<topic> \n <gap> \n <method> \n <conclusion>",
         "type": "[Business]"
     }
    },
    {"title": "08 - A new criterion for assessing discriminant validity in variance-based structural equation modeling",
     "content": {
        "abstract": "<topic> Discriminant validity assessment </topic> <gap> has become a generally accepted prerequisite for analyzing relationships between latent variables. For variance-based structural equation modeling, such as partial least squares, the Fornell-Larcker criterion and the examination of cross-loadings are the dominant approaches for evaluating discriminant validity. </gap> <method> By means of a simulation study, </method> <goal> we show that these approaches do not reliably detect the lack of discriminant validity in common research situations. </goal> <method> We therefore propose an alternative approach, based on the multitrait-multimethod matrix, to assess discriminant validity: the heterotrait-monotrait ratio of correlations. We demonstrate its superior performance by means of a Monte Carlo simulation study, in which we compare the new approach to the Fornell-Larcker criterion and the assessment of (partial) cross-loadings. </method> <conclusion> Finally, we provide guidelines on how to handle discriminant validity issues in variance-based structural equation modeling. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <method> \n <goal> \n <method> \n <conclusion>",
        "type": "[Business]"
    }
    },
    {"title": "09 - Virtual Teams Research: 10 Years, 10 Themes, and 10 Opportunities",
     "content": {
         "abstract": "<gap> Ten years ago, Martins, Gilson, and Maynard reviewed the emerging <topic> virtual team (VT) </topic> literature. Given the proliferation of new communication technologies and the increased usage of work teams, it is hardly surprising that the last decade has seen an influx of VT research. </gap> <method> In this review, we organize the last 10 years of empirical work around 10 main themes: research design, team inputs, team virtuality, technology, globalization, leadership, mediators and moderators, trust, outcomes, and ways to enhance VT success. These themes emerged inductively because they either represent areas with consistent results, a large proliferation of studies, or a grouping of studies and results that differed from where the literature stood a decade ago. Following the review section, we turn our attention toward 10 opportunities for future research: study setting, generational impacts, methodological considerations, new and emerging technologies, member mobility, subgroups, team adaptation, transition processes and planning, creativity, and team member well-being. Some of these opportunities emerged from our review of the extant VT literature; others are grounded in the broader team literature, are unresolved theoretical issues, or were linked to insights discussed within the VT practitioner literature. </method> <conclusion> Within the domain of VTs, technological innovation continues to advance the way team members interact and enable individuals who previously could not be connected to work together as a team. Accordingly, VTs provide great promise to organizations, and the field continues to be rich with research opportunities for the coming decade(s). </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion>",
         "type": "[Business]"
     }
    },
    {"title": "10 - Understanding Customer Experience Throughout the Customer Journey",
     "content": {
        "abstract": "<topic> Understanding customer experience and the customer journey </topic> <gap> over time is critical for firms. Customers now interact with firms through myriad touch points in multiple channels and media, and customer experiences are more social in nature. These changes require firms to integrate multiple business functions, and even external partners, in creating and delivering positive customer experiences. </gap> <goal> In this article, the authors aim to develop a stronger understanding of customer experience and the customer journey in this era of increasingly complex customer behavior. To achieve this goal, </goal> <method> they examine existing definitions and conceptualizations of customer experience as a construct and provide a historical perspective of the roots of customer experience within marketing. Next, they attempt to bring together what is currently known about customer experience, customer journeys, and customer experience management. </method> <conclusion> Finally, they identify critical areas for future research on this important topic. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Business]"
     }
    },
    {"title": "11 - Graphitic Carbon Nitride (g-C3N4)-Based Photocatalysts for Artificial Photosynthesis and Environmental Remediation: Are We a Step Closer To   Achieving Sustainability?",
     "content": {
        "abstract": "<gap> As a fascinating conjugated polymer, <topic> graphitic carbon nitride </topic> (g-C3N4) has become a new research hotspot and drawn broad interdisciplinary attention as a metal-free and visible-light-responsive photocatalyst in the arena of solar energy conversion and environmental remediation. This is due to its appealing electronic band structure, high physicochemical stability, and \"earth-abundant\" nature. </gap> <goal> This critical review summarizes a panorama of the latest progress related to the design and construction of pristine g-C3N4 and g-C3N4-based nanocomposites, </goal> <method> including (1) nanoarchitecture design of bare g-C3N4, such as hard and soft templating approaches, supramolecular preorganization assembly, exfoliation, and template-free synthesis routes, (2) functionalization of g-C3N4 at an atomic level (elemental doping) and molecular level (copolymerization), and (3) modification of g-C3N4 with well-matched energy levels of another semiconductor or a metal as a cocatalyst to form heterojunction nanostructures. The construction and characteristics of each classification of the heterojunction system will be critically reviewed, namely metal-g-C3N4, semiconductor-g-C3N4, isotype g-C3N4/g-C3N4, graphitic carbon-g-C3N4, conducting polymer-g-C3N4, sensitizer-g-C3N4, and multicomponent heterojunctions. The band structures, electronic properties, optical absorption, and interfacial charge transfer of g-C3N4-based heterostructured nanohybrids will also be theoretically discussed based on the first-principles density functional theory (DFT) calculations to provide insightful outlooks on the charge carrier dynamics. Apart from that, the advancement of the versatile photoredox applications toward artificial photosynthesis (water splitting and photofixation of CO2), environmental decontamination, and bacteria disinfection will be presented in detail. Last but not least, this comprehensive review will conclude with a summary and some invigorating perspectives on the challenges and future directions at the forefront of this research platform. </method> <conclusion> It is anticipated that this review can stimulate a new research doorway to facilitate the next generation of gC(3)N(4)-based photocatalysts with ameliorated performances by harnessing the outstanding structural, electronic, and optical properties for the development of a sustainable future without environmental detriment. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Chemistry]"
     }
    },
    {"title": "12 - Noble metal-free hydrogen evolution catalysts for water splitting",
     "content": {
        "abstract": "<topic> Sustainable hydrogen production </topic> <gap> is an essential prerequisite of a future hydrogen economy. Water electrolysis driven by renewable resource-derived electricity and direct solar-to-hydrogen conversion based on photochemical and photoelectrochemical water splitting are promising pathways for sustainable hydrogen production. All these techniques require, among many things, highly active noble metal-free hydrogen evolution catalysts to make the water splitting process more energy-efficient and economical. </gap> <goal> In this review, we highlight the recent research efforts toward the synthesis of noble metal-free electrocatalysts, especially at the nanoscale, and their catalytic properties for the hydrogen evolution reaction (HER). </goal> <method> We review several important kinds of heterogeneous non-precious metal electrocatalysts, including metal sulfides, metal selenides, metal carbides, metal nitrides, metal phosphides, and heteroatom-doped nanocarbons. In the discussion, emphasis is given to the synthetic methods of these HER electrocatalysts, the strategies of performance improvement, and the structure/composition-catalytic activity relationship. We also summarize some important examples showing that non-Pt HER electrocatalysts could serve as efficient cocatalysts for promoting direct solar-to-hydrogen conversion in both photochemical and photoelectrochemical water splitting systems, when combined with suitable semiconductor photocatalysts. </method>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method>",
        "type": "[Chemistry]"
    }
    },
    {"title": "13 - Cesium-containing triple cation perovskite solar cells: improved    stability, reproducibility and high efficiency",
     "content": {
        "abstract": "<gap> Today's best <topic> perovskite solar cells </topic> use a mixture of formamidinium and methylammonium as the monovalent cations. <method> With the addition of inorganic cesium, </method> <conclusion> the resulting triple cation perovskite compositions are thermally more stable, contain less phase impurities and are less sensitive to processing conditions. This enables more reproducible device performances to reach a stabilized power output of 21.1% and similar to 18% after 250 hours under operational conditions. </conclusion> These properties are key for the industrialization of perovskite photovoltaics. </gap>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion> \n <gap>",
        "type": "[Chemistry]"
     }
    },
    {"title": "14 - Towards greener and more sustainable batteries for electrical energy  storage",
     "content": {
         "abstract": "<gap> Ever-growing energy needs and depleting fossil-fuel resources demand the pursuit of <topic> sustainable energy alternatives, </topic> including both renewable energy sources and sustainable storage technologies. It is therefore essential to incorporate material abundance, eco-efficient synthetic processes and life-cycle analysis into the design of new electrochemical storage systems. At present, a few existing technologies address these issues, but in each case, fundamental and technological hurdles remain to be overcome. </gap> <goal> Here we provide an overview of the current state of energy storage from a sustainability perspective. </goal> <method> We introduce the notion of sustainability through discussion of the energy and environmental costs of state-of-the-art lithium-ion batteries, considering elemental abundance, toxicity, synthetic methods and scalability. With the same themes in mind, we also highlight current and future electrochemical storage systems beyond lithium-ion batteries. The complexity and importance of recycling battery materials is also discussed. </method>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method>",
         "type": "[Chemistry]"
     }
    },
    {"title": "15 - Free Polymer Solar Cells with over 11% Efficiency and Excellent Thermal Stability",
     "content": {
         "abstract": "<method> A nonfullerene-based polymer solar cell (PSC) that significantly outperforms fullerene-based PSCs with respect to the power-conversion efficiency is demonstrated for the first time. </method> <conclusion> An efficiency of >11%, which is among the top values in the PSC field, and excellent thermal stability is obtained using PBDB-T and ITIC as donor and acceptor, respectively. </conclusion>",
         "macrostructure": "<method> \n <conclusion>",
         "type": "[Chemistry]"
     }
    },
    {"title": "16 - Moving beyond 'Next Wednesday': The interplay of lexical semantics and  constructional meaning in an ambiguous metaphoric statement",
     "content": {
        "abstract": "<gap> What factors influence our <topic> understanding of metaphoric statements </topic> about time? By examining the interpretation of one such statement - namely, Next Wednesday's meeting has been moved forward by two days - earlier research has demonstrated that people may draw on spatial perspectives, involving multiple spatially based temporal reference strategies, to interpret metaphoric statements about time (e.g. Boroditsky 2000; Kranjec 2006; McGlone and Harding 1998; Nunez et al. 2006). However, what is still missing is an understanding of the role of linguistic factors in the interpretation of temporal statements such as this one. </gap> <goal> In this paper, we examine the linguistic properties of this famous temporally ambiguous utterance, considered as an instantiation of a more schematic construction. </goal> <method> In Experiment 1, we examine the roles of individual lexical items that are used in the utterance in order to better understand the interplay of lexical semantics and constructional meaning in the context of a metaphoric statement. Following up on prior suggestions in the literature, we ask whether the locus of the ambiguity is centred on the adverb, centred on the verb, or distributed across the utterance. <conclusion> The results suggest that the final interpretation results from an interplay of verb and adverb, suggesting a distributed temporal semantics analogous to the distributed semantics noted for the metaphoric source domain of space (Sinha and Kuteva 1995) and consistent with a constructional view of language (Goldberg 2003). In Experiment 2, we expand the linguistic factors under investigation to include voice and person. </method> The findings suggest that grammatical person, but not grammatical voice, may also influence the interpretation of the Next Wednesday's meeting metaphor. Taken together, the results of these two studies illuminate the interplay of lexical and constructional factors in the interpretation of temporal metaphors. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion> \n <method> \n <conclusion>",
        "type": "[Cognitive Linguistics]"
     }
    },
    {"title": "17 - Visualizing onomasiological change: Diachronic variation in metonymic patterns for WOMAN in Chinese",
     "content": {
        "abstract": "<goal> This paper introduces an innovative method to aid the study of <topic> conceptual onomasiological </topic> research, with a specific emphasis on diachronic variation in the metonymic patterns with which a target concept is expressed. </goal> <method> We illustrate how the method is applied to explore and visualize such diachronic changes by means of a case study on the metonymic patterns for WOMAN in the history of Chinese. Visualization is done with the help of a Multidimensional Scaling solution based on the profile-based distance calculation (Geeraerts et al. 1999; Speelman et al. 2003) and by drawing diachronic trajectories in a set of MDS maps, corresponding to different metonymic targets. This method proves to be effective and feasible in detecting changes in the distribution of metonymic patterns in authentic historical corpus data. On the basis of this method, we can show that different targets exhibit different degrees of diachronic variation in their metonymic patterns. We find diachronically more stable targets (e.g. IMPERIAL WOMAN), targets with a dominant trend in diachronic variation (e.g. A WOMAN), and targets with highly fluctuating historical variation (e.g. BEAUTIFUL WOMAN). Importantly, we can identify the cultural and social changes that may lie behind some of these changes. </method> <conclusion> Examining the results uncovered by the method offers us a better understanding of the dynamicity of metonymic conceptualizations. </conclusion>",
        "macrostructure": "<goal> \n <topic> \n <goal> \n <method> \n <conclusion>",
        "type": "[Cognitive Linguistics]"
     }
    },
    {"title": "18 - Cognitive Grammar and gesture: Points of convergence, advances and challenges",
     "content": {
         "abstract": "<gap> Given its usage-oriented character, <topic> Cognitive Grammar (CG) </topic> can be expected to be consonant with a multimodal, rather than text-only, perspective on language. Whereas several scholars have acknowledged this potential, the question as to how speakers' gestures can be incorporated in CG-based grammatical analysis has not been conclusively addressed. </gap> <goal> In this paper, we aim to advance the CG-gesture relationship. </goal> <method> We first elaborate on three important points of convergence between CG and gesture research: (1) CG's conception of grammar as a prototype category, with central and more peripheral structures, aligns with the variable degrees to which speakers' gestures are conventionalized in human communication. (2) Conceptualization, which lies at the basis of grammatical organization according to CG, is known to be of central importance for gestural expression. In fact, all of the main dimensions of construal postulated in CG (specificity, perspective, profile-base relationship, conceptual archetypes) receive potential gestural expression. (3) CG's intensive use of diagrammatic notation allows for the incorporation of spatial features of gestures. Subsequently, we demonstrate how CG can be applied to analyze the structure of multimodal, spoken-gestured utterances. </method> <conclusion> These analyses suggest that the constructs and tools developed by CG can be employed to analyze the compositionality that exists within a single gesture (between conventional and more idiosyncratic components) as well as in the grammatical relations that may exist between gesture and speech. Finally, we raise a number of theoretical and empirical challenges. </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
         "type": "[Cognitive Linguistics]"
     }
    },
    {"title": "19 - Constructional meaning representation within a knowledge engineering framework",
     "content": {
         "abstract": "<gap> FunGramKB is a multipurpose lexico-conceptual knowledge base for natural language processing systems, and more particularly, for natural language understanding. The linguistic layer of this <topic> knowledge-engineering project is grounded in compatible aspects of two linguistic accounts, namely, Role and Reference Grammar (RRG) and the Lexical Constructional Model (LCM). RRG, although originally a lexicalist approach, has recently incorporated constructional configurations </topic> into its descriptive and explanatory apparatus. The LCM has sought to understand from its inception the factors that constrain lexical-constructional integration. </gap> <goal> Within this theoretical context, this paper discusses the format of lexical entries, highly inspired in RRG proposals, and of constructional schemata, which are organized </goal> <method> according to the descriptive levels supplied by the LCM. Both lexical and constructional structure is represented by means of Attribute Value Matrices (AVMs). Thus, the lexical and grammatical levels of FunGramKB are the focus of our attention here. Additionally, the need for a conceptualist approach to meaning construction is highlighted throughout our discussion. </method>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method>",
         "type": "[Cognitive Linguistics]"
     }
    },
    {"title": "20 - Operationalizing mirativity A usage-based quantitative study of constructional construal in English",
     "content": {
        "abstract": "<topic> This study focuses on the conceptual category of mirativity and its constructional construal in English. </topic> <goal> We propose an operationalization of mirativity with a view to investigating the phenomenon </goal> <method> within the usage-based quantitative methodology of multifactorial analysis (Geeraerts, Grondelaers, & Bakema, 1994; Gries, 2003). The proposed operationalization is founded on two usage dimensions, i.e., the degree of performativity of the utterance and the degree of incongruity of the described event. It is argued that mirativity, in its prototypical form, can be operationally defined as a combination of high levels of these two variables. The feasibility of this operationalization in usage-based quantitative research is tested in a case study investigating three surprise-encoding constructions in English: [what + the + NP], [what + a + NP] and [to + my + NP]. The data, amounting to 350 observations of the three constructions, were extracted from dialogic online diaries and submitted to detailed manual annotation and subsequent multivariate statistical modeling. </method> <conclusion> The results reveal a usage continuum ranging from [what + the + NP] through [to + my + NP] to [what + a + NP] relative to the high degrees of performativity and incongruity. </conclusion>",
        "macrostructure": "<topic> \n <goal> \n <method> \n <conclusion>",
        "type": "[Cognitive Linguistics]"
     }
    },
    {"title": "21 - Fitting Linear Mixed-Effects Models Using lme4",
     "content": {
         "abstract": "<gap> Maximum likelihood or restricted maximum likelihood (REML) estimates of the parameters in <topic> linear mixed-effects models </topic> can be determined using the lmer function in the lme4 package for R. As for most model-fitting functions in R, the model is described in an lmer call by a formula, in this case including both fixed- and random-effects terms. The formula and data together determine a numerical representation of the model from which the profiled deviance or the profiled REML criterion can be evaluated as a function of some of the model parameters. The appropriate criterion is optimized, using one of the constrained optimization functions in R, to provide the parameter estimates. </gap> <method> We describe the structure of the model, the steps in evaluating the profiled deviance or REML criterion, and the structure of classes or types that represents such a model. Sufficient detail is included </method> <conclusion> to allow specialization of these structures by users who wish to write functions to fit specialized linear mixed models, such as models incorporating pedigrees or smoothing splines, that are not easily expressible in the formula language used by lmer. </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion>",
         "type": "[Computer Science]"
     }
    },
    {"title": "22 - Deep Convolutional Neural Networks for Computer-Aided Detection: CNN   Architectures, Dataset Characteristics and Transfer Learning",
     "content": {
        "abstract": "<gap> Remarkable progress has been made in <topic> image recognition, </topic> primarily due to the availability of large-scale annotated datasets and deep convolutional neural networks (CNNs). CNNs enable learning data-driven, highly representative, hierarchical image features from sufficient training data. However, obtaining datasets as comprehensively annotated as ImageNet in the medical imaging domain remains a challenge. There are currently three major techniques that successfully employ CNNs to medical image classification: training the CNN from scratch, using off-the-shelf pre-trained CNN features, and conducting unsupervised CNN pre-training with supervised fine-tuning. Another effective method is transfer learning, i.e., fine-tuning CNN models pre-trained from natural image dataset to medical image tasks. </gap> <goal> In this paper, we exploit three important, but previously understudied factors of employing deep convolutional neural networks to computer-aided detection problems. </goal> <method> We first explore and evaluate different CNN architectures. The studied models contain 5 thousand to 160 million parameters, and vary in numbers of layers. We then evaluate the influence of dataset scale and spatial image context on performance. Finally, we examine when and why transfer learning from pre-trained ImageNet (via fine-tuning) can be useful. We study two specific computer-aided detection (CADe) problems, namely thoraco-abdominal lymph node (LN) detection and interstitial lung disease (ILD) classification. </method> <conclusion> We achieve the state-of-the-art performance on the mediastinal LN detection, and report the first five-fold cross-validation classification results on predicting axial CT slices with ILD categories. Our extensive empirical evaluation, CNN model analysis and valuable insights can be extended to the design of high performance CAD systems for other medical imaging tasks. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Computer Science]"
     }
    },
    {"title": "23 - Structural Damage Detection Using Modal Strain Energy and Hybrid  Multiobjective Optimization",
     "content": {
         "abstract": "<gap> Modal strain energy (MSE) is a sensitive physical property that can be utilized as </gap> <topic> a damage index in structural health monitoring. </topic> <gap> Inverse problem solving-based approaches using single-objective optimization algorithms are also a promising damage identification method. However, the research into the integration of these methods is currently limited; only partial success in the detection of structural damage with high errors has been reported. The majority of previous research was focused on detecting damage in simply supported beams or plain structures. </gap> <goal> In this study, a novel damage detection approach </goal> <method> using hybrid multiobjective optimization algorithms based on MSE  </method> <goal> is proposed to detect damages in various three-dimensional (3-D) steel structures. </goal> <conclusion> Minor damages have little effect on the difference of the modal properties of the structure, and thus such damages with multiple locations in a structure are difficult to detect using traditional damage detection methods based on modal properties. Various minor damage scenarios are created for the 3-D structures to investigate the newly proposed multiobjective approach. The proposed hybrid multiobjective genetic algorithm detects the exact locations and extents of the induced minor damages in the structure. Even though it uses incomplete mode shapes, which do not have any measured information at the damaged element, the proposed approach detects damage well. The robustness of the proposed method is investigated by adding 5% Gaussian random white noise as a noise effect to mode shapes, which are used in the calculation ofMSE. </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <goal> \n <conclusion>",
         "type": "[Computer Science]"
     }
    },
    {"title": "24 - A Survey on Demand Response in Smart Grids: Mathematical Models and Approaches",
     "content": {
        "abstract": "<gap> The <topic> smart grid </topic> is widely considered to be the informationization of the power grid. As an essential characteristic of the smart grid, demand response can reschedule the users' energy consumption to reduce the operating expense from expensive generators, and further to defer the capacity addition in the long run. </gap> <goal> This survey comprehensively explores four major aspects: 1) programs; 2) issues; 3) approaches; and 4) future extensions of demand response. </goal> <method> Specifically, we first introduce the means/ tariffs that the power utility takes to incentivize users to reschedule their energy usage patterns. Then we survey the existing mathematical models and problems in the previous and current literatures, followed by the state- of- the- art approaches and solutions to address these issues. Finally, based on the above overview, we also outline the potential challenges and </method> <conclusion> future research directions in the context of demand response. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Computer Science]"
    }
    },
    {"title": "25 - Trainable COSFIRE filters for vessel delineation with application to retinal images",
     "content": {
        "abstract": "<topic> Retinal imaging </topic> <gap> provides a non-invasive opportunity for the diagnosis of several medical pathologies. The automatic segmentation of the vessel tree is an important pre-processing step which facilitates subsequent automatic processes that contribute to such diagnosis. </gap> <goal> We introduce a novel method for the automatic segmentation of vessel trees in retinal fundus images. We propose a filter that selectively responds to vessels and that we call B-COSFIRE with B standing for bar which is an abstraction for a vessel. </goal> <method>  It is based on the existing COSFIRE (Combination Of Shifted Filter Responses) approach. A B-COSFIRE filter achieves orientation selectivity by computing the weighted geometric mean of the output of a pool of Difference-of-Gaussians filters, whose supports are aligned in a collinear manner. It achieves rotation invariance efficiently by simple shifting operations. The proposed filter is versatile as its selectivity is determined from any given vessel-like prototype pattern in an automatic configuration process. We configure two B-COSFIRE filters, namely symmetric and asymmetric, that are selective for bars and bar-endings, respectively. We achieve vessel segmentation by summing up the responses of the two rotation-invariant B-COSFIRE filters followed by thresholding. </method> <conclusion> The results that we achieve on three publicly available data sets (DRIVE: Se = 0.7655, Sp = 0.9704; STARE: Se = 0.7716, Sp = 0.9701; CHASE_DB1: Se = 0.7585, Sp = 0.9587) are higher than many of the state-of-the-art methods. The proposed segmentation approach is also very efficient with a time complexity that is significantly lower than existing methods. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Computer Science]"
     }
    },
    {"title": "26 - Free vibration analysis of nonlocal strain gradient beams made of functionally graded material",
     "content": {
        "abstract": "<gap> A size-dependent Timoshenko beam model, which accounts for through-thickness power law variation of a two-constituent functionally graded (FG) material, is derived in the framework of the nonlocal strain gradient theory. The equations of motion and boundary conditions are deduced by employing the Hamilton principle. The model contains a material length scale parameter introduced to consider the significance of strain gradient stress field and a nonlocal parameter introduced to consider the significance of nonlocal elastic stress field. </gap> <goal> The influence of through-thickness power-law variation and size-dependent parameters on vibration is investigated. </goal> <conclusion> It is found that through-thickness grading of the FG material in the beam has a great effect on the natural frequencies and therefore can be used to control the natural frequencies. The vibration frequencies can generally increase with the increasing material length scale parameter or the decreasing nonlocal parameter. When the material characteristic parameter is smaller than the nonlocal parameter, the FG beam exerts a stiffness-softening effect. When the material characteristic parameter is larger than the nonlocal parameter, the FG beam exerts a stiffness-hardening effect. </conclusion>",
        "macrostructure": "<gap> \n <goal> \n <conclusion>",
        "type": "[Engineering]"
     }
    },
    {"title": "27 - Topology Optimization in Aircraft and Aerospace Structures Design",
     "content": {
         "abstract": "<topic> Topology optimization </topic> <gap> has become an effective tool for least-weight and performance design, especially  </gap> <topic> in aeronautics and aerospace engineering. </topic> <goal> The purpose of this paper is to survey recent advances of topology optimization techniques applied in aircraft and aerospace structures design. </goal> <method> This paper firstly reviews several existing applications: (1) standard material layout design for airframe structures, (2) layout design of stiffener ribs for aircraft panels, (3) multi-component layout design for aerospace structural systems, (4) multi-fasteners design for assembled aircraft structures. Secondly, potential applications of topology optimization in dynamic responses design, shape preserving design, smart structures design, structural features design and additive manufacturing are introduced to provide a forward-looking perspective. </method>",
         "macrostructure": "<topic> \n <gap> \n <topic> \n <goal> \n <method>",
         "type": "[Engineering]"
     }
    },
    {"title": "28 - Mechanical and tribological properties of self-lubricating metal matrix nanocomposites reinforced by carbon nanotubes (CNTs) and graphene – A review",
     "content": {
        "abstract": "<gap> Rapid innovation in nanotechnology in recent years enabled development of advanced metal matrix nanocomposites for structural engineering and functional devices. </gap> <topic> Carbonous materials, such as graphite, carbon nanotubes (CNT's), and graphene possess unique electrical, mechanical, and thermal properties. </topic> <gap> Owe to their lubricious nature, these carbonous materials have attracted researchers to synthesize lightweight self-lubricating metal matrix nanocomposites with superior mechanical and tribological properties for several applications in automotive and aerospace industries. </gap> <goal> This review focuses on the recent development in mechanical and tribological behavior of self-lubricating metallic nanocomposites reinforced by carbonous nanomaterials such as CNT and graphene. </goal> <method> The review includes development of self-lubricating nanocomposites, related issues in their processing, their characterization, and investigation of their tribological behavior. </method> <conclusion> The results reveal that adding CNT and graphene to metals decreases both coefficient of friction and wear rate as well as increases the tensile strength. The mechanisms involved for the improved mechanical and tribological behavior is discussed. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Engineering]"
     }
    },
    {"title": "29 - A comprehensive experimental and modeling study of isobutene oxidation",
     "content": {
         "abstract": "<topic> Isobutene <gap>  is an important intermediate in the pyrolysis and oxidation </topic> of higher-order branched alkanes, and it is also a component of commercial gasolines. </gap> <goal> To better understand its combustion characteristics, </goal> <method> a series of ignition delay time (IDT) and laminar flame speed (LFS) measurements have been performed. In addition, flow reactor speciation data recorded for the pyrolysis and oxidation of isobutene is also reported. Predictions of an updated kinetic model described herein are compared with each of these data sets, as well as with existing jet-stirred reactor (JSR) species measurements.    IDTs of isobutene oxidation were measured in four different shock tubes and in two rapid compression machines (RCMs) under conditions of relevance to practical combustors. The combination of shock tube and RCM data greatly expands the range of available validation data for isobutene oxidation models to pressures of 50 atm and temperatures in the range 666-1715 K. Isobutene flame speeds were measured experimentally at 1 atm and at unburned gas temperatures of 298-398 K over a wide range of equivalence ratios. For the flame speed results, there was good agreement between different facilities and the current model in the fuel-rich region. Ab initio chemical kinetics calculations were carried out to calculate rate constants for important reactions such as H-atom abstraction by hydroxyl and hydroperoxyl radicals and the decomposition of 2-methylallyl radicals.    A comprehensive chemical kinetic mechanism has been developed to describe the combustion of isobutene and is validated by comparison to the presently considered experimental measurements. Important reactions, highlighted via flux and sensitivity analyses, include: (a) hydrogen atom abstraction from isobutene by hydroxyl and hydroperoxyl radicals, and molecular oxygen; (b) radical-radical recombination reactions, including 2-methylallyl radical self-recombination, the recombination of 2-methylallyl radicals with hydroperoxyl radicals; and the recombination of 2-methylallyl radicals with methyl radicals; (c) addition reactions, including hydrogen atom and hydroxyl radical addition to isobutene; and (d) 2-methylallyl radical decomposition reactions. The current mechanism accurately predicts the IDT and LFS measurements presented in this study, as well as the JSR and flow reactor speciation data already available in the literature.    The differences in low-temperature chemistry between alkanes and alkenes are also highlighted. in this work. In normal alkanes, the fuel radical (R) over dot adds to molecular oxygen forming alkylperoxyl (R(O) over dot(2)) radicals followed by isomerization and chain branching reactions which promote low-temperature fuel reactivity. However, in alkenes, because of the relatively shallow well (similar to 20 kcal mol(-1)) for R(O) over dot(2) formation compared to similar to 35 kcal mol(-1) in alkanes, the (R) over dot+O-2 (sic) R(O) over dot(2) equilibrium lies more to the left favoring (R) over dot+O-2 rather than R(O) over dot(2) radical stabilization. </method> <conclusion> Based on this work, and related studies of allylic systems, it is apparent that reactivity for alkene components at very low temperatures (<800 K) emanates from hydroxyl radical addition followed by addition of molecular oxygen to radical. At intermediate temperatures (800-1300 K), alkene reactivity is controlled by hydrogen abstraction by molecular oxygen and the reactions between resonantly stabilized radicals and hydroperoxyl radicals which results in chain branching. At higher temperatures (>1300 K), the reactivity is mainly governed by the competition between hydrogen abstractions by molecular oxygen and OH radicals. </conclusion>",
         "macrostructure": "<topic> \n <gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
         "type": "[Engineering]"
     }
    },
    {"title": "30 - Nanofluid flow and heat transfer between parallel plates considering  Brownian motion using DTM",
     "content": {
         "abstract": "<gap> The problem of <topic> nanofluid hydrothermal behavior </topic> in presence of variable magnetic field is investigated analytically using Differential Transformation Method. The fluid in the enclosure is water containing different types of nanoparticles: Al2O3 and CuO. The effective thermal conductivity and viscosity of nanofluid are calculated by KKL (Koo-Kleinstreuer-Li) correlation.  </gap> <goal> In this model effect of Brownian motion on the effective thermal conductivity is considered. </goal> <method> The comparison between the results from Differential Transformation Method and previous work are in well agreement which proved the capability of this method for solving such problems. The effect of the squeeze number, nanofluid volume fraction, Hartmann number and heat source parameter on flow and heat transfer is investigated. </method> <conclusion> The results show that skin friction coefficient increases with increase of the squeeze number and Hartmann number but it decreases with increase of nanofluid volume fraction. Nusselt number increases with augment of nanoparticle volume fraction, Hartmann number while it decreases with increase of the squeeze number. </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
         "type": "[Engineering]"
     }
    },
    {"title": "31 - Coproduction of healthcare service",
     "content": {
        "abstract": "<gap> Efforts to ensure effective <topic> participation of patients in healthcare </topic> are called by many names -patient centredness, patient engagement, patient experience. Improvement initiatives in this domain often resemble the efforts of manufacturers to engage consumers in designing and marketing products. Services, however, are fundamentally different than products; unlike goods, services are always 'coproduced'. Failure to recognise this unique character of a service and its implications may limit our success in partnering with patients to improve health care. </gap> <method> We trace a partial history of the coproduction concept, present a model of healthcare service coproduction and explore its application as a design principle in three healthcare service delivery innovations. We use the principle to examine the roles, relationships and aims of this interdependent work. We explore the principle's implications and challenges </method> <goal> for health professional development, for service delivery system design and for understanding and measuring benefit in healthcare services. </goal>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <goal>",
        "type": "[Health Care Sciences and Services]"
     }
    },
    {"title": "32 - The Mass Production of Redundant, Misleading, and Conflicted Systematic   Reviews and Meta-analyses",
     "content": {
        "abstract": "<gap> Currently, <topic> there is massive production of unnecessary, misleading, and conflicted systematic reviews and meta-analyses. </topic> Instead of promoting evidence-based medicine and health care, these instruments often serve mostly as easily produced publishable units or marketing tools. Suboptimal systematic reviews and meta-analyses can be harmful given the major prestige and influence these types of studies have acquired. The publication of systematic reviews and meta-analyses should be realigned to remove biases and vested interests and to integrate them better with the primary production of evidence. </gap> \n <gap> Context \n Currently, most systematic reviews and meta-analyses are done retrospectively with fragmented published information. </gap> <goal> This article aims to explore the growth of published systematic reviews and meta-analyses and to estimate how often they are redundant, misleading, or serving conflicted interests. </goal> \n <method> Methods \n Data included information from PubMed surveys and from empirical evaluations of meta-analyses. </method> \n <conclusion> Findings \n Publication of systematic reviews and meta-analyses has increased rapidly. In the period January 1, 1986, to December 4, 2015, PubMed tags 266,782 items as systematic reviews and 58,611 as meta-analyses. Annual publications between 1991 and 2014 increased 2,728% for systematic reviews and 2,635% for meta-analyses versus only 153% for all PubMed-indexed items. Currently, probably more systematic reviews of trials than new randomized trials are published annually. Most topics addressed by meta-analyses of randomized trials have overlapping, redundant meta-analyses; same-topic meta-analyses may exceed 20 sometimes. Some fields produce massive numbers of meta-analyses; for example, 185 meta-analyses of antidepressants for depression were published between 2007 and 2014. These meta-analyses are often produced either by industry employees or by authors with industry ties and results are aligned with sponsor interests. China has rapidly become the most prolific producer of English-language, PubMed-indexed meta-analyses. The most massive presence of Chinese meta-analyses is on genetic associations (63% of global production in 2014), where almost all results are misleading since they combine fragmented information from mostly abandoned era of candidate genes. Furthermore, many contracting companies working on evidence synthesis receive industry contracts to produce meta-analyses, many of which probably remain unpublished. Many other meta-analyses have serious flaws. Of the remaining, most have weak or insufficient evidence to inform decision making. Few systematic reviews and meta-analyses are both non-misleading and useful. \n Conclusions \n The production of systematic reviews and meta-analyses has reached epidemic proportions. Possibly, the large majority of produced systematic reviews and meta-analyses are unnecessary, misleading, and/or conflicted. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Health Care Sciences and Services]"
     }
    },
    {"title": "33 - Cost-Effectiveness Analysis Alongside Clinical Trials II-An ISPOR Good    Research Practices Task Force Report",
     "content": {
        "abstract": "<topic> Clinical trials <gap> evaluating medicines, medical devices, and procedures now commonly assess the economic value of these interventions. </topic> The growing number of prospective clinical/economic trials reflects both widespread interest in economic information for new technologies and the regulatory and reimbursement requirements of many countries that now consider evidence of economic value along with clinical efficacy. As decision makers increasingly demand evidence of economic value for health care interventions, conducting high-quality economic analyses alongside clinical studies is desirable because they broaden the scope of information available on a particular intervention, and can efficiently provide timely information with high internal and, when designed and analyzed properly, reasonable external validity. In 2005, ISPOR published the Good Research Practices for Cost Effectiveness Analysis Alongside Clinical Trials: The ISPOR RCTCEA 'I'ask Force report ISPOR initiated an update of the report in 2014 to include the methodological developments over the last 9 years. </gap> <method> This report provides updated recommendations reflecting advances in several areas related to trial design, selecting data elements, database design and management, analysis, and reporting of results. </method> <conclusion> Task force members note that trials should be designed to evaluate effectiveness (rather than efficacy) when possible, should include clinical outcome measures, and should obtain health resource use and health state utilities directly from study subjects. Collection of economic data should be fully integrated into the study. An incremental analysis should be conducted with an intention-to-treat approach, complemented by relevant subgroup analyses. Uncertainty should be characterized. Articles should adhere to established standards for reporting results of cost-effectiveness analyses. Economic studies alongside trials are complementary to other evaluations (e.g., modeling studies) as information for decision makers who consider evidence of economic value along with clinical efficacy when making resource allocation decisions. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <topic> \n <gap> \n <method> \n <conclusion>",
        "type": "[Health Care Sciences and Services]"
     }
    },
    {"title": "34 - Food Insecurity And Health Outcomes",
     "content": {
        "abstract": "<gap> Almost fifty million people are food insecure in the United States, which makes <topic> food insecurity one of the nation's leading health and nutrition issues. </gap> </topic> <goal> We examine recent research evidence of the health consequences of food insecurity for children, nonsenior adults, and seniors in the United States. </goal> <method> For context, we first provide an overview of how food insecurity is measured in the country, followed by a presentation of recent trends in the prevalence of food insecurity. Then we present a survey of selected recent research that examined the association between food insecurity and health outcomes. We show that the literature has consistently found food insecurity to be negatively associated with health. For example, after confounding risk factors were controlled for, studies found that food-insecure children are at least twice as likely to report being in fair or poor health and at least 1.4 times more likely to have asthma, compared to food-secure children; and food-insecure seniors have limitations in activities of daily living comparable to those of food-secure seniors fourteen years older. </method> <conclusion> The Supplemental Nutrition Assistance Program (SNAP) substantially reduces the prevalence of food insecurity and thus is critical to reducing negative health outcomes. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <topic> \n <goal> \n <method> \n <conclusion>",
        "type": "[Health Care Sciences and Services]"
     }
    },
    {"title": "35 - The Effect of an Intervention to Break the Gender Bias Habit for Faculty   at One Institution: A Cluster Randomized, Controlled Trial",
     "content": {
         "abstract": "<goal> Purpose \n <gap> Despite sincere commitment to egalitarian, meritocratic principles, subtle gender bias persists, constraining women's opportunities for academic advancement. </gap> The authors implemented a pair-matched, single-blind, cluster randomized, controlled study of a gender-bias-habit-changing intervention at a large public university. </goal> \n <method> Method \n Participants were faculty in 92 departments or divisions at the University of Wisconsin Madison. Between September 2010 and March 2012, experimental departments were offered a gender-bias-habit-changing intervention as a 2.5-hour workshop. Surveys measured gender bias awareness; motivation, self-efficacy, and outcome expectations to reduce bias; and gender equity action. A timed word categorization task measured implicit gender/leadership bias. Faculty completed a work life survey before and after all experimental departments received the intervention. Control departments were offered workshops after data were collected. </method> \n <conclusion> Results \n Linear mixed-effects models showed significantly greater changes post intervention for faculty in experimental versus control departments on several outcome measures, including self-efficacy to engage in gender-equity-promoting behaviors (P=.013). When 25% of a department's faculty attended the workshop (26 of 46 departments), significant increases in self-reported action to promote gender equity occurred at three months (P =.007). Post intervention, faculty in experimental departments expressed greater perceptions of fit (P=.024), valuing of their research (P=.019), and comfort in raising personal and professional conflicts (P =.025). \n Conclusions \n An intervention that facilitates intentional behavioral change can help faculty break the gender bias habit and change department climate in ways that should support the career advancement of women in academic medicine, science, and engineering. </conclusion> \n",
         "macrostructure": "<goal> \n <gap> \n <goal> \n <method> \n <conclusion>",
         "type": "[Health Care Sciences and Services]"
     }
    },
    {"title": "36 - Identity and a Model of Investment in Applied Linguistics",
     "content": {
         "abstract": "<gap> This article locates Norton's foundational work <topic> on identity and investment within the social turn of applied linguistics. </topic> It discusses its historical impetus and theoretical anchors, and it illustrates how these ideas have been taken up in recent scholarship. In response to the demands of the new world order, spurred by technology and characterized by mobility, </gap> <method> it proposes a comprehensive model of investment, which occurs at the intersection of identity, ideology, and capital. </method> <conclusion> The model recognizes that the spaces in which language acquisition and socialization take place have become increasingly deterritorialized and unbounded, and the systemic patterns of control more invisible. This calls for new questions, analyses, and theories of identity. The model addresses the needs of learners who navigate their way through online and offline contexts and perform identities that have become more fluid and complex. As such, it proposes a more comprehensive and critical examination of the relationship between identity, investment, and language learning. <method> Drawing on two case studies of a female language learner in rural Uganda and a male language learner in urban Canada, </method> the model illustrates how structure and agency, operating across time and space, can accord or refuse learners the power to speak. </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion> \n <method> \n <conclusion>",
         "type": "[Linguistics]"
     }
    },
    {"title": "37 - Academic publishing and the myth of linguistic injustice",
     "content": {
         "abstract": "<gap> Academic publication now dominates the lives of academics across the globe who must increasingly submit their research for publication in high profile English language journals to move up the career ladder. <topic> The dominance of English in academic publishing, </topic> however, has raised questions of communicative inequality and <topic> the possible 'linguistic injustice' </topic> against an author's mother tongue. Native English speakers are thought to have an advantage as they acquire the language naturalistically while second language users must invest more time, effort and money into formally learning it and may experience greater difficulties when writing in English. Attitude surveys reveal that English as an Additional Language authors often believe that editors and referees are prejudiced against them for any non-standard language. </gap> <goal> In this paper, I critically review the evidence for linguistic Injustice </goal> <method> through a survey of the literature and interviews with scholars working in Hong Kong.  </method> <conclusion> I argue that framing publication problems as a crude Native vs non-Native polarization not only draws on an outmoded respect for 'Native speaker' competence but serves to demoralizes EAL writers and marginalize the difficulties experienced by novice Ll English academics. The paper, then, is a call for a more inclusive and balanced view of academic publishing. </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
         "type": "[Linguistics]"
     }
    },
    {"title": "38 - The Effectiveness of L2 Pronunciation Instruction: A Narrative Review",
     "content": {
        "abstract": "<gap> Research on the efficacy of second language  <topic> (L2) pronunciation instruction </topic> has produced mixed results, despite reports of significant improvement in many studies. Possible explanations for divergent outcomes include learner individual differences, goals and foci of instruction, type and duration of instructional input, and assessment procedures. </gap> <method> After identifying key concepts, we survey 75 L2 pronunciation studies, particularly their methods and results. Despite a move towards emphasizing speech intelligibility and comprehensibility, most research surveyed promoted native-like pronunciation as the target. Although most studies entailed classroom instruction, many featured Computer Assisted Pronunciation Teaching (CAPT). Segmentals were studied more often than suprasegmentals. The amount of instruction required to effect change was related to researchers' goals; interventions focusing on a single feature were generally shorter than those addressing more issues. Reading-aloud tasks were the most common form of assessment; very few studies measured spontaneous speech. The attribution of improvement as a result of instruction was compromised in some instances by lack of a control group. </method> <conclusion> We summarize our findings, highlight limitations of current research, and offer suggestions for future directions. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion>",
        "type": "[Linguistics]"
     }
    },
    {"title": "39 - Fast oscillatory dynamics during language comprehension: Unification    versus maintenance and prediction?",
     "content": {
        "abstract": "<gap> The role of <topic> neuronal oscillations during language comprehension </topic> is not yet well understood. </gap> <goal> In this paper we review and reinterpret the functional roles of beta-and gamma-band oscillatory activity during language comprehension at the sentence and discourse level. </goal> <method> We discuss the evidence in favor of a role for beta and gamma in unification (the unification hypothesis), and in light of mounting evidence that cannot be accounted for under this hypothesis, we explore an alternative proposal linking beta and gamma oscillations to maintenance and prediction (respectively) during language comprehension. Our maintenance/prediction hypothesis is able to account for most of the findings that are currently available relating beta and gamma oscillations to language comprehension, and is in good agreement with other proposals about the roles of beta and gamma in domain-general cognitive processing. </method> <conclusion> In conclusion we discuss proposals for further testing and comparing the prediction and unification hypotheses. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Linguistics]"
     }
    },
    {"title": "40 - Statistical learning as an individual ability: Theoretical perspectives and empirical evidence",
     "content": {
        "abstract": "<gap> Although the power of <topic> statistical learning (SL) in explaining a wide range of linguistic functions </topic> is gaining increasing support, relatively little research has focused on this theoretical construct from the perspective of individual differences. However, to be able to reliably link individual differences in a given ability such as language learning to individual differences in SL, three critical theoretical questions should be posed: Is SL a componential or unified ability? Is it nested within other general cognitive abilities? Is it a stable capacity of an individual? </gap> <method>  Following an initial mapping sentence outlining the possible dimensions of SL, we employed a battery of SL tasks in the visual and auditory modalities, using verbal and non-verbal stimuli, with adjacent and non-adjacent contingencies. SL tasks were administered along with general cognitive tasks in a within-subject design at two time points to explore our theoretical questions. </method> <conclusion> We found that SL, as measured by some tasks, is a stable and reliable capacity of an individual. Moreover, we found SL to be independent of general cognitive abilities such as intelligence or working memory. However, SL is not a unified capacity, so that individual sensitivity to conditional probabilities is not uniform across modalities and stimuli. </conclusion>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion>",
        "type": "[Linguistics]"
     }
    },
    {"title": "41 - Spin Hall effects",
     "content": {
        "abstract": "<topic> Spin Hall effects </topic> <gap> are a collection of relativistic spin-orbit coupling phenomena in which electrical currents can generate transverse spin currents and vice versa. Despite being observed only a decade ago, these effects are already ubiquitous within spintronics, as standard spin-current generators and detectors. </gap> <goal> Here the theoretical and experimental results that have established this subfield of spintronics are reviewed. </goal> <method> The focus is on the results that have converged to give us the current understanding of the phenomena, which has evolved from a qualitative to a more quantitative measurement of spin currents and their associated spin accumulation. Within the experimental framework, optical-, transport-, and magnetization-dynamics-based measurements are reviewed and linked to both phenomenological and microscopic theories of the effect. Within the theoretical framework, the basic mechanisms in both the extrinsic and intrinsic regimes are reviewed, which are linked to the mechanisms present in their closely related phenomenon in ferromagnets, the anomalous Hall effect. Also reviewed is the connection to the phenomenological treatment based on spin-diffusion equations applicable to certain regimes, as well as the spin-pumping theory of spin generation used in many measurements of the spin Hall angle. A further connection to the spin-current-generating spin Hall effect to the inverse spin galvanic effect is given, in which an electrical current induces a nonequilibrium spin polarization. This effect often accompanies the spin Hall effect since they share common microscopic origins. Both can exhibit the same symmetries when present in structures comprising ferromagnetic and nonmagnetic layers through their induced current-driven spin torques or induced voltages. Although a short chronological overview of the evolution of the spin Hall effect field and the resolution of some early controversies is given, the main body of this review is structured from a pedagogical point of view, focusing on well-established and accepted physics. </method> <conclusion> In such a young field, there remains much to be understood and explored, hence some of the future challenges and opportunities of this rapidly evolving area of spintronics are outlined. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Physics]"
     }
    },
    {"title": "42 - Magnon spintronics",
     "content": {
        "abstract": "<topic> Magnon spintronics </topic> <gap> is the field of spintronics concerned with structures, devices and circuits that use spin currents carried by magnons. Magnons are the quanta of spin waves: the dynamic eigen-excitations of a magnetically ordered body. Analogous to electric currents, magnon-based currents can be used to carry, transport and process information. The use of magnons allows the implementation of novel wave-based computing technologies free from the drawbacks inherent to modern electronics, such as dissipation of energy due to Ohmic losses. Logic circuits based on wave interference and nonlinear wave interaction can be designed with much smaller footprints compared with conventional electron-based logic circuits. </gap> <goal> In this review, <method> after an introduction into the basic properties of magnons and their handling, </method> we discuss the inter-conversion between magnon currents and electron-carried spin and charge currents; and concepts and experimental studies of magnon-based computing circuits. </goal>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <goal>",
        "type": "[Physics]"
     }
    },
    {"title": "43 - Reactive species in non-equilibrium atmospheric-pressure plasmas:  Generation, transport, and biological effects",
     "content": {
        "abstract": "<topic> Non-equilibrium atmospheric-pressure plasmas </topic> <gap> have recently become a topical area of research owing to their diverse applications in health care and medicine, environmental remediation and pollution control, materials processing, electrochemistry, nanotechnology and other fields. </gap> <goal> This review focuses on the reactive electrons and ionic, atomic, molecular, and radical species that are produced in these plasmas and then transported from the point of generation to the point of interaction with the material, medium, living cells or tissues being processed. </goal> <method> The most important mechanisms of generation and transport of the key species in the plasmas of atmospheric-pressure plasma jets and other non-equilibrium atmospheric-pressure plasmas are introduced and examined from the viewpoint of their applications in plasma hygiene and medicine and other relevant fields. Sophisticated high precision, time-resolved plasma diagnostics approaches and techniques are presented and their applications to monitor the reactive species and plasma dynamics in the plasma jets and other discharges, both in the gas phase and during the plasma interaction with liquid media, are critically reviewed. The large amount of experimental data is supported by the theoretical models of reactive species generation and transport in the plasmas, surrounding gaseous environments, and plasma interaction with liquid media. These models are presented and their limitations are discussed. Special attention is paid to biological effects of the plasma-generated reactive oxygen and nitrogen (and some other) species in basic biological processes such as cell metabolism, proliferation, survival, etc. as well as plasma applications in bacterial inactivation, wound healing, cancer treatment and some others. Challenges and opportunities for theoretical and experimental research are discussed and the authors' vision for the emerging convergence trends across several disciplines and </method>  <conclusion> application domains is presented to stimulate critical discussions and collaborations in the future. </conclusion>",
        "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
        "type": "[Physics]"
     }
    },
    {"title": "44 - Experimental Discovery of Weyl Semimetal TaAs",
     "content": {
         "abstract": "<topic> Weyl semimetals </topic> <gap> are a class of materials that can be regarded as three-dimensional analogs of graphene upon breaking time-reversal or inversion symmetry. Electrons in a Weyl semimetal behave as Weyl fermions, which have many exotic properties, such as chiral anomaly and magnetic monopoles in the crystal momentum space. The surface state of a Weyl semimetal displays pairs of entangled Fermi arcs at two opposite surfaces. However, the existence of Weyl semimetals has not yet been proved experimentally. </gap> <goal> Here, we report the experimental realization of a Weyl semimetal in TaAs </goal> <method> by observing Fermi arcs formed by its surface states using angle-resolved photoemission spectroscopy. </method> <conclusion> Our first-principles calculations, which match remarkably well with the experimental results, further confirm that TaAs is a Weyl semimetal. </conclusion>",
         "macrostructure": "<topic> \n <gap> \n <goal> \n <method> \n <conclusion>",
         "type": "[Physics]"
     }
    },
    {"title": "45 - Physics of microswimmers-single particle motion and collective behavior:    a review",
     "content": {
        "abstract": "<gap> Locomotion and transport of microorganisms in fluids is an essential aspect of life. Search for food, orientation toward light, spreading of off-spring, and the formation of colonies are only possible due to locomotion. <topic> Swimming at the microscale </topic> occurs at low Reynolds numbers, where fluid friction and viscosity dominates over inertia. Here, evolution achieved propulsion mechanisms, which overcome and even exploit drag. Prominent propulsion mechanisms are rotating helical flagella, exploited by many bacteria, and snake-like or whip-like motion of eukaryotic flagella, utilized by sperm and algae. For artificial microswimmers, alternative concepts to convert chemical energy or heat into directed motion can be employed, which are potentially more efficient. The dynamics of microswimmers comprises many facets, which are all required to achieve locomotion. </gap> <goal>  In this article, we review the physics of locomotion of biological and synthetic microswimmers, and the collective behavior of their assemblies. </goal> <method> Starting from individual microswimmers, we describe the various propulsion mechanism of biological and synthetic systems and address the hydrodynamic aspects of swimming. This comprises synchronization and the concerted beating of flagella and cilia. In addition, the swimming behavior next to surfaces is examined. Finally, collective and cooperate phenomena of various types of isotropic and anisotropic swimmers with and without hydrodynamic interactions are discussed. </method>",
        "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method>",
        "type": "[Physics]"
     }
    },
    {"title": "46 - Internet of Things: A Survey on Enabling Technologies, Protocols, and    Applications",
     "content": {
         "abstract": "<goal> This paper provides an overview of the Internet of Things (IoT) with emphasis on enabling technologies, protocols, and application issues. </goal> <topic> The IoT is enabled by the latest developments in RFID, smart sensors, communication technologies, and Internet protocols. </topic> <gap> The basic premise is to have smart sensors collaborate directly without human involvement to deliver a new class of applications. The current revolution in Internet, mobile, and machine-to-machine (M2M) technologies can be seen as the first phase of the IoT. In the coming years, the IoT is expected to bridge diverse technologies to enable new applications by connecting physical objects together in support of intelligent decision making. </gap> <method> This paper starts by providing a horizontal overview of the IoT. Then, we give an overview of some technical details that pertain to the IoT enabling technologies, protocols, and applications. Compared to other survey papers in the field, our objective is to provide a more thorough summary of the most relevant protocols and application issues to enable researchers and application developers to get up to speed quickly on how the different protocols fit together to deliver desired functionalities without having to go through RFCs and the standards specifications. We also provide an overview of some of the key IoT challenges presented in the recent literature and provide a summary of related research work. Moreover, we explore the relation between the IoT and other emerging technologies including big data analytics and cloud and fog computing. We also present the need for better horizontal integration among IoT services. Finally, we present detailed service use-cases to illustrate </method> <conclusion> how the different protocols presented in the paper fit together to deliver desired IoT services. </conclusion>",
         "macrostructure": "<goal> \n <topic> \n <gap> \n <method> \n <conclusion>",
         "type": "[Telecommunications]"
     }
    },
    {"title": "47 - Non-Orthogonal Multiple Access for 5G: Solutions, Challenges, Opportunities, and Future Research Trends",
     "content": {
        "abstract": "<gap> The increasing demand of mobile Internet and the Internet of Things poses challenging requirements for 5G wireless communications, such as high spectral efficiency and massive connectivity. </gap> <goal> In this article, a promising technology, <topic> non-orthogonal multiple access (NOMA), </topic> is discussed, which can address some of these challenges for 5G. </goal> <method> Different from conventional orthogonal multiple access technologies, NOMA can accommodate much more users via non-orthogonal resource allocation. We divide existing dominant NOMA schemes into two categories: power-domain multiplexing and code-domain multiplexing, and the corresponding schemes include power-domain NOMA, multiple access with low-density spreading, sparse code multiple access, multi-user shared access, pattern division multiple access, and so on. We discuss their principles, key features, and pros/cons, and then provide a comprehensive comparison of these solutions from the perspective of spectral efficiency, system performance, receiver complexity, and so on. In addition, challenges, opportunities, and future research trends for NOMA design are highlighted to provide some insight on the potential future work for researchers in this field. Finally, to leverage different multiple access schemes including both conventional OMA and new NOMA, we propose the concept of software defined multiple access (SoDeMA), which </method> <conclusion> enables adaptive configuration of available multiple access schemes to support diverse services and applications in future 5G networks. </conclusion>",
        "macrostructure": "<gap> \n <goal> \n <topic> \n <goal> \n <method> \n <conclusion>",
        "type": "[Telecommunications]"
     }
    },
    {"title": "48 - LTE-UNLICENSED: THE FUTURE OF SPECTRUM AGGREGATION FOR CELLULAR NETWORKS",
     "content": {
         "abstract": "<gap> The phenomenal growth of mobile data demand has brought about increasing scarcity in available <topic> radio spectrum. </topic> Meanwhile, mobile customers pay more attention to their own experience, especially in communication reliability and service continuity on the move. To address these issues, LTE-Unlicensed, or LTE-U, is considered one of the latest groundbreaking innovations to provide high performance and seamless user experience under a unified radio technology by extending LTE to the readily available unlicensed spectrum. </gap> <method> In this article, we offer a comprehensive overview of the LTE-U technology from both operator and user perspectives, and examine its impact on the incumbent unlicensed systems. Specifically, we first introduce the implementation regulations, principles, and typical deployment scenarios of LTE-U. Potential benefits for both operators and users are then discussed. We further identify three key challenges in bringing LTE-U into reality together with related research directions. In particular, the most critical issue of LTE-U is coexistence with other unlicensed systems, such as widely deployed WiFi. The LTE/WiFi coexistence mechanisms are elaborated in time, frequency, and power aspects, respectively. </method> <conclusion> Simulation results demonstrate that LTE-U can provide better user experience to LTE users while well protecting the incumbent WiFi users' performance compared to two existing advanced technologies: cellular/WiFi interworking and licensed-only heterogeneous networks (Het-Nets). </conclusion>",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <method> \n <conclusion>",
         "type": "[Telecommunications]"
     }
    },
    {"title": "49 - System Architecture and Key Technologies for 5G Heterogeneous Cloud  Radio Access Networks",
     "content": {
         "abstract": "<gap> Compared with fourth generation cellular systems, <topic> fifth generation wireless communication </topic> systems are anticipated to provide spectral and energy efficiency growth by a factor of at least 10, and the area throughput growth by a factor of at least 25. </gap> <goal> To achieve these goals, a H-CRAN is presented in this article as the advanced wireless access network paradigm, </goal> <method> where cloud computing is used to fulfill the centralized large-scale cooperative processing for suppressing co-channel interferences. The state-of-the-art research achievements in the areas of system architecture and key technologies for H-CRANs are surveyed. Particularly, Node C as a new communication entity is defined to converge the existing ancestral base stations and act as the base band unit pool to manage all accessed remote radio heads. Also, the software-defined H-CRAN system architecture is presented to be compatible with software-defined networks. The principles, performance gains, and open issues of key technologies, including adaptive large-scale cooperative spatial signal processing, cooperative radio resource management, network function virtualization, and self-organization, are summarized. The major challenges in terms of fronthaul constrained resource allocation optimization and energy harvesting that may affect the promotion of H-CRANs are discussed as well. </method> ",
         "macrostructure": "<gap> \n <topic> \n <gap> \n <goal> \n <method>",
         "type": "[Telecommunications]"
     }
    },
    {"title": "50 - Cooperative Non-orthogonal Multiple Access With Simultaneous Wireless Information and Power Transfer",
     "content": {
        "abstract": "<goal> In this paper, the application of simultaneous  <topic> wireless information and power transfer </topic>  (SWIPT) to nonorthogonal multiple access (NOMA) networks in which users are spatially randomly located is investigated. A new co-operative SWIPT NOMA protocol is proposed, in which near NOMA users that are close to the source act as energy harvesting relays to help far NOMA users. </goal>  <goal> Since the locations of users have a significant impact on the performance, </goal>  <method> three user selection schemes based on the user distances from the base station are proposed. To characterize the performance of the proposed selection schemes, closed-form expressions for the outage probability and system throughput are derived. </method> <conclusion> These analytical results demonstrate that the use of SWIPT will not jeopardize the diversity gain compared to the conventional NOMA. The proposed results confirm that the opportunistic use of node locations for user selection can achieve low outage probability and deliver superior throughput in comparison to the random selection scheme. </conclusion>",
        "macrostructure": "<goal> \n <topic> \n <goal> \n <method> \n <conclusion>",
        "type": "[Telecommunications]"
     }
    },
    '''
    {"title": "",
     "content": {
        "topic": "",
        "gap": "",
        "goal": "",
        "method": "",
        "conclusion": "",
        "abstract": "",
        "macrostructure": "",
        "type": "[]"
    }
    },
    '''
]

print("Abstracts:")
for abstract in abstracts:
    print(shorten(abstract, width=70))

num_escolha = input("\nType in the number of the abstract you want to tag: ")
num = int(num_escolha) - 1
type_choice = 0

#TRANSFORMA O ABSTRACT EM UM ARRAY, CADA PALAVRA EM UMA POSIÇÃO DO ARRAY
abstract_array = abstractsTagged[num]["content"]["abstract"].split()

#AQUI O CÓDIGO PEGA A POSIÇÃO INICIAL E FINAL DE CADA UMA DAS PARTES DO TEXTO
#SÃO INICIADAS COMO -1 PARA QUE CASO UMA DAS PARTES NÃO EXISTA ESCREVA 'N/A'
topic_i = -1
topic_f = -1
gap_i = -1
gap_f = -1
goal_i = -1
goal_f = -1
method_i = -1
method_f = -1
conclusion_i = -1
conclusion_f = -1
cont = 0
for a in abstract_array:
    if(a == "<topic>"):
        topic_i = cont
    if (a == "</topic>"):
        topic_f = cont
    if (a == "<gap>"):
        gap_i = cont
    if (a == "</gap>"):
        gap_f = cont
    if (a == "<goal>"):
        goal_i = cont
    if (a == "</goal>"):
        goal_f = cont
    if (a == "<method>"):
        method_i = cont
    if (a == "</method>"):
        method_f = cont
    if (a == "<conclusion>"):
        conclusion_i = cont
    if (a == "</conclusion>"):
        conclusion_f = cont
    cont = cont + 1

cont=1

#AQUI O CÓDIGO COLOCA O FRAME UMA POSIÇÃO A FRENTE DO ITEM LEXICAL
abstract_frame = abstractsTagged[num]["content"]["abstract"].split()

with open("frames.csv", "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv, delimiter=",")
    for coluna in leitor:
        if(coluna["abstract_name"] == (abstractsTagged[num]["title"])[5:]):
            aux=0
            for a in abstract_frame:
                if(coluna["lexical_unit"] == a):
                    frame = "<"+coluna["frame"]+">"
                    if(abstract_frame[aux+1] != frame):
                        abstract_frame.insert((aux + 1), "<" + coluna["frame"] + ">")
                        break
                aux = aux + 1
            cont = cont + 1

#AQUI O CÓDIGO PEGA A POSIÇÃO INICIAL E FINAL DE CADA UMA DAS PARTES DO TEXTO COM FRAMES
#SÃO INICIADAS COMO -1 PARA QUE CASO UMA DAS PARTES NÃO EXISTA ESCREVA 'N/A'
topic_frame_i = -1
topic_frame_f = -1
gap_frame_i = -1
gap_frame_f = -1
goal_frame_i = -1
goal_frame_f = -1
method_frame_i = -1
method_frame_f = -1
conclusion_frame_i = -1
conclusion_frame_f = -1
cont = 0
for a in abstract_frame:
    if(a == "<topic>"):
        topic_frame_i = cont
    if (a == "</topic>"):
        topic_frame_f = cont
    if (a == "<gap>"):
        gap_frame_i = cont
    if (a == "</gap>"):
        gap_frame_f = cont
    if (a == "<goal>"):
        goal_frame_i = cont
    if (a == "</goal>"):
        goal_frame_f = cont
    if (a == "<method>"):
        method_frame_i = cont
    if (a == "</method>"):
        method_frame_f = cont
    if (a == "<conclusion>"):
        conclusion_frame_i = cont
    if (a == "</conclusion>"):
        conclusion_frame_f = cont
    cont = cont + 1

while(type_choice != "15"):
    print("----------------------------------------------------------------------")
    print(fill(abstractsTagged[num]["content"]["type"]+" "+abstractsTagged[num]["title"], width=70))
    print("----------------------------------------------------------------------")
    print("Choices:")
    print("01 - full abstract")
    print("02 - full abstract with frames")
    print("03 - title")
    print("04 - macrostructure")
    print("05 - topic")
    print("06 - topic with frames")
    print("07 - gap")
    print("08 - gap with frames")
    print("09 - purpose")
    print("10 - purpose with frames")
    print("11 - method")
    print("12 - method with frames")
    print("13 - conclusion")
    print("14 - conclusion with frames")
    print("15 - exit")
    print("----------------------------------------------------------------------")
    type_choice = input("Type the choice: ")
    print("")

    #FULL ABSTRACT
    if(type_choice == "1"):
        abstract = fill(abstractsTagged[num]["content"]["abstract"], width=70)
        print(abstract)

    #FULL ABSTRACT WITH FRAMES
    elif(type_choice == "2"):
        abstract_frame_text = " "
        for a in abstract_frame:
            abstract_frame_text = abstract_frame_text + " " + a
        print(fill(abstract_frame_text, width=70))

    #TITLE
    elif (type_choice == "3"):
        title = fill((abstractsTagged[num]["title"])[5:], width=70)
        print(title)

    #MACROSTRUCTURE
    elif(type_choice == "4"):
        macrostructure = fill(abstractsTagged[num]["content"]["macrostructure"], width=70)
        print(" "+abstractsTagged[num]["content"]["macrostructure"])

    #TOPIC
    elif(type_choice == "5"):
        text_topic = " "
        if(topic_i != -1 and topic_f != -1):
            aux = topic_i
            while(aux <= topic_f):
                text_topic = text_topic + " " +abstract_array[aux]
                aux = aux + 1
        else:
            text_topic = "N/A"
        print(fill(text_topic, width=70))

    #TOPIC WITH FRAMES
    elif (type_choice == "6"):
        text_topic_frame = " "
        if (topic_frame_i != -1 and topic_frame_f != -1):
            aux = topic_frame_i
            while (aux <= topic_frame_f):
                text_topic_frame = text_topic_frame + " " + abstract_frame[aux]
                aux = aux + 1
        else:
            text_topic_frame = "N/A"
        print(fill(text_topic_frame, width=70))

    #GAP
    elif(type_choice == "7"):
        text_gap = " "
        if (gap_i != -1 and gap_f != -1):
            aux = gap_i
            while (aux <= gap_f):
                text_gap = text_gap + " " + abstract_array[aux]
                aux = aux + 1
        else:
            text_gap = "N/A"
        print(fill(text_gap, width=70))

    #GAP WITH FRAMES
    elif (type_choice == "8"):
        text_gap_frame = " "
        if (gap_frame_i != -1 and gap_frame_f != -1):
            aux = gap_frame_i
            while (aux <= gap_frame_f):
                text_gap_frame = text_gap_frame + " " + abstract_frame[aux]
                aux = aux + 1
        else:
            text_gap_frame = "N/A"
        print(fill(text_gap_frame, width=70))

    #GOAL
    elif(type_choice == "9"):
        text_goal = " "
        if (goal_i != -1 and goal_f != -1):
            aux = goal_i
            while (aux <= goal_f):
                text_goal = text_goal + " " + abstract_array[aux]
                aux = aux + 1
        else:
            text_goal = "N/A"
        print(fill(text_goal, width=70))

    #GOAL WITH FRAMES
    elif (type_choice == "10"):
        text_goal_frame = " "
        if (goal_frame_i != -1 and goal_frame_f != -1):
            aux = goal_frame_i
            while (aux <= goal_frame_f):
                text_goal_frame = text_goal_frame + " " + abstract_frame[aux]
                aux = aux + 1
        else:
            text_goal_frame = "N/A"
        print(fill(text_goal_frame, width=70))

    #METHOD
    elif(type_choice == "11"):
        text_method = " "
        if (method_i != -1 and method_f != -1):
            aux = method_i
            while (aux <= method_f):
                text_method = text_method + " " + abstract_array[aux]
                aux = aux + 1
        else:
            text_method = "N/A"
        print(fill(text_method, width=70))

    #METHOD WITH FRAMES
    elif (type_choice == "12"):
        text_method_frame = " "
        if (method_frame_i != -1 and method_frame_f != -1):
            aux = method_frame_i
            while (aux <= method_frame_f):
                text_method_frame = text_method_frame + " " + abstract_frame[aux]
                aux = aux + 1
        else:
            text_method_frame = "N/A"
        print(fill(text_method_frame, width=70))

    #CONCLUSION
    elif(type_choice == "13"):
        text_conclusion = " "
        if (conclusion_i != -1 and conclusion_f != -1):
            aux = conclusion_i
            while (aux <= conclusion_f):
                text_conclusion = text_conclusion + " " + abstract_array[aux]
                aux = aux + 1
        else:
            text_conclusion = "N/A"
        print(fill(text_conclusion, width=70))

    #CONCLUSION WITH FRAMES
    elif (type_choice == "14"):
        text_conclusion_frame = " "
        if (conclusion_frame_i != -1 and conclusion_frame_f != -1):
            aux = conclusion_frame_i
            while (aux <= conclusion_frame_f):
                text_conclusion_frame = text_conclusion_frame + " " + abstract_frame[aux]
                aux = aux + 1
        else:
            text_conclusion_frame = "N/A"
        print(fill(text_conclusion_frame, width=70))

    elif(type_choice == "15"):
        print("You choose to leave. See you later!")
        break

    else:
        print("Invalid Option")
