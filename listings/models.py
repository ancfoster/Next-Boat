from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

# Create your models here.
class Listings(models.Model):
    #Choice lists
    LISTING_STATUS_CHOICES = [('A', 'Available'), ('P', 'Pending Sale'), ('S', 'Sold'), ('N', 'Not Listed')]
    TAX_PAID_CHOICES = [('Y', 'Tax Paid'), ('N', 'Tax Unpaid')]
    CONDITION_CHOICES = [('N', 'New'), ('U', 'Used')]
    BOAT_TYPE = [('P', 'Power'), ('S', 'Sail')]
    HULL_MATERIAL = [('F', 'Fibreglass/GRP'), ('S', 'Steel'), ('W', 'Wood'), ('A', 'Aluminium'), ('O', 'Other')]
    HULL_CONFIG = [('M', 'Monohull'), ('C', 'Catamaran'), ('T', 'Trimaran')]
    FUEL = [('D', 'Diesel' ), ('P', 'Petrol'), ('E', 'Electric'), ('N', 'None')]
    CATEGORY_CHOICES = [('PC', 'Planing Cruiser'),
        ('DC', 'Displacement Cruiser'),
        ('S', 'Sport'),
        ('F', 'Fishing'),
        ('RT', 'RIB/Tender'),
        ('NC', 'Narrow/Canal'),
        ('C', 'Cruiser'),
        ('DS', 'Day Sailer'),
        ('DI', 'Dinghy'),
        ('RA', 'Racing'),
        ]

    COUNTRIES = [('BE', 'Belgium'),
        ('CA', 'Canada'),
        ('DE', 'Denmark'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('GE', 'Germany'),
        ('GI', 'Gibraltar'),
        ('GE', 'Greece'),
        ('IR', 'Republic of Ireland'),
        ('IT', 'Italy'),
        ('MA', 'Malta'),
        ('NE', 'Netherlands'),
        ('NO', 'Norway'),
        ('PO', 'Poland'),
        ('PR', 'Portugal'),
        ('ES', 'Spain'),
        ('SV', 'Sweden'),
        ('TK', 'Turkey'),
        ('UK', 'United Kingdom'),
        ('US', 'United States')]

    BOAT_MODELS_LIST = [
        ('M1', 'AB Inflatables'),
        ('M2', 'ACM'),
        ('M3', 'ATX Surf Boats'),
        ('M4', 'Absolute'),
        ('M5', 'Achilles'),
        ('M6', 'Action Craft'),
        ('M7', 'Advantage'),
        ('M8', 'Aicon'),
        ('M9', 'Alalunga'),
        ('M10', 'Albemarle'),
        ('M11', 'Albin'),
        ('M12', 'Albury Brothers'),
        ('M13', 'Alerion'),
        ('M14', 'Alfastreet Marine'),
        ('M15', 'Allmand'),
        ('M16', 'Altair'),
        ('M17', 'Alu Marine'),
        ('M18', 'Alumacraft'),
        ('M19', 'Alumaweld'),
        ('M20', 'Alva Yachts'),
        ('M21', 'Alweld'),
        ('M22', 'American Tug'),
        ('M23', 'Angler'),
        ('M24', 'Antaris'),
        ('M25', 'Apreamare'),
        ('M26', 'AquaPatio'),
        ('M27', 'Aquador'),
        ('M28', 'Aquasport'),
        ('M29', 'Aquila'),
        ('M30', 'Arcadia Yachts'),
        ('M31', 'Archambault'),
        ('M32', 'Arcoa'),
        ('M33', 'Arcona'),
        ('M34', 'Argos Nautic'),
        ('M35', 'Arima'),
        ('M36', 'Ascend'),
        ('M37', 'Avalon'),
        ('M38', 'Avenger'),
        ('M39', 'Aviara'),
        ('M40', 'Avid'),
        ('M41', 'Avon'),
        ('M42', 'Axis'),
        ('M43', 'Azimut'),
        ('M44', 'Back Cove'),
        ('M45', 'Baja'),
        ('M46', 'Barge'),
        ('M47', 'Barletta'),
        ('M48', 'Barracuda'),
        ('M49', 'Bass Cat'),
        ('M50', 'Bavaria'),
        ('M51', 'Bay Craft'),
        ('M52', 'Bayliner'),
        ('M53', 'Belize'),
        ('M54', 'Belzona'),
        ('M55', 'Beneteau'),
        ('M56', 'Beneteau America'),
        ('M57', 'Bennington'),
        ('M58', 'Bentley Pontoons'),
        ('M59', 'Bering'),
        ('M60', 'Berkshire'),
        ('M61', 'Bertram'),
        ('M62', 'Birchwood'),
        ('M63', 'BlackJack'),
        ('M64', 'BlackWater'),
        ('M65', 'Blackfin'),
        ('M66', 'Blazer'),
        ('M67', 'Blue Wave'),
        ('M68', 'Bluewater Sportfishing'),
        ('M69', 'Bombard'),
        ('M70', 'Boston Whaler'),
        ('M71', 'Brig'),
        ('M72', 'Brizo'),
        ('M73', 'Broadblue'),
        ('M74', 'Broom'),
        ('M75', 'Bruckmann'),
        ('M76', 'Bryant'),
        ('M77', 'Buddy Davis'),
        ('M78', 'Bulls Bay'),
        ('M79', 'C&C'),
        ('M80', 'C-Dory'),
        ('M81', 'C-Hawk'),
        ('M82', 'CL Yachts'),
        ('M83', 'CRN'),
        ('M84', 'Cabo'),
        ('M85', 'Cabo Rico'),
        ('M86', 'Caliber'),
        ('M87', 'Campion'),
        ('M88', 'Canados'),
        ('M89', 'Cape Horn'),
        ('M90', 'Capelli'),
        ('M91', 'Caravelle'),
        ('M92', 'Carolina Classic'),
        ('M93', 'Carolina Skiff'),
        ('M94', 'Carver'),
        ('M95', 'Catalina'),
        ('M96', 'Catamaran'),
        ('M97', 'Catana'),
        ('M98', 'Caymas'),
        ('M99', 'Centurion'),
        ('M100', 'Century'),
        ('M101', 'Champion'),
        ('M102', 'Chaparral'),
        ('M103', 'Checkmate'),
        ('M104', 'Cheoy Lee'),
        ('M105', 'Chris-Craft'),
        ('M106', 'Classic'),
        ('M107', 'Clearwater'),
        ('M108', 'Coastal Craft'),
        ('M109', 'Cobalt'),
        ('M110', 'Cobia'),
        ('M111', 'Cobra Ribs'),
        ('M112', 'Colombo'),
        ('M113', 'Columbia'),
        ('M114', 'Com-Pac'),
        ('M115', 'Compass'),
        ('M116', 'Concept'),
        ('M117', 'Conrad'),
        ('M118', 'Contender'),
        ('M119', 'Contest'),
        ('M120', 'Cormorant Yachts'),
        ('M121', 'Cornish Crabbers'),
        ('M122', 'Correct Craft'),
        ('M123', 'Corsair'),
        ('M124', 'Cranchi'),
        ('M125', 'Crescent'),
        ('M126', 'Crest'),
        ('M127', 'Crestliner'),
        ('M128', 'Crevalle'),
        ('M129', 'Crownline'),
        ('M130', 'Cruisers Yachts'),
        ('M131', 'Custom'),
        ('M132', 'Custom Carolina'),
        ('M133', 'Custom Line'),
        ('M134', 'Custom Weld'),
        ('M135', 'Cutwater'),
        ('M136', 'Cypress Cay'),
        ('M137', 'Dale'),
        ('M138', 'DeFever'),
        ('M139', 'Deep Impact'),
        ('M140', 'Defiance'),
        ('M141', 'Dehler'),
        ('M142', 'Delphia'),
        ('M143', 'Delta Powerboats'),
        ('M144', 'Discovery'),
        ('M145', 'Dominator'),
        ('M146', 'Donzi'),
        ('M147', 'Dorado'),
        ('M148', 'Doral'),
        ('M149', 'Dromeas'),
        ('M150', 'Duckworth'),
        ('M151', 'Dufour'),
        ('M152', 'Dutch Barge'),
        ('M153', 'Dyer'),
        ('M154', 'Dyna'),
        ('M155', 'Eagle'),
        ('M156', 'Eastern'),
        ('M157', 'Ebbtide'),
        ('M158', 'Edgewater'),
        ('M159', 'Egg Harbor'),
        ('M160', 'Elan'),
        ('M161', 'Elan Power'),
        ('M162', 'Elegance'),
        ('M163', 'Elling'),
        ('M164', 'Eolo'),
        ('M165', 'Epic'),
        ('M166', 'Everglades'),
        ('M167', 'Excel'),
        ('M168', 'Explorer'),
        ('M169', 'Extreme Boats'),
        ('M170', 'Faeton'),
        ('M171', 'Fairline'),
        ('M172', 'Farr'),
        ('M173', 'Feeling'),
        ('M174', 'Ferretti Yachts'),
        ('M175', 'Filippetti Yacht'),
        ('M176', 'Finseeker'),
        ('M177', 'Fisher'),
        ('M178', 'Fjord'),
        ('M179', 'Flats Cat'),
        ('M180', 'Formula'),
        ('M181', 'Fountain'),
        ('M182', 'Fountaine Pajot'),
        ('M183', 'Four Winns'),
        ('M184', 'Fratelli Aprea'),
        ('M185', 'Freedom'),
        ('M186', 'Front Runner'),
        ('M187', 'Frontier'),
        ('M188', 'G3'),
        ('M189', 'Gala'),
        ('M190', 'Galeon'),
        ('M191', 'Gekko'),
        ('M192', 'Gib Sea'),
        ('M193', 'Gibson'),
        ('M194', 'Glacier Bay'),
        ('M195', 'Glasstream'),
        ('M196', 'Glastron'),
        ('M197', 'Gobbi'),
        ('M198', 'Godfrey'),
        ('M199', 'Grady-White'),
        ('M200', 'Grand Banks'),
        ('M201', 'Grand Harbour'),
        ('M202', 'Grand Soleil'),
        ('M203', 'Greenline'),
        ('M204', 'Gulet'),
        ('M205', 'Gulf Craft'),
        ('M206', 'Gulf Crosser'),
        ('M207', 'HCB'),
        ('M208', 'HH Catamarans'),
        ('M209', 'Hallberg-Rassy'),
        ('M210', 'Hampton'),
        ('M211', 'Hans Christian'),
        ('M212', 'Hanse'),
        ('M213', 'Hardy'),
        ('M214', 'Harris'),
        ('M215', 'Harris FloteBote'),
        ('M216', 'Harris-Kayot'),
        ('M217', 'Hatteras'),
        ('M218', 'Henriques'),
        ('M219', 'Hewes'),
        ('M220', 'Hewescraft'),
        ('M221', 'Heyday'),
        ('M222', 'Heysea'),
        ('M223', 'Hi-Star'),
        ('M224', 'Highfield'),
        ('M225', 'Hinckley'),
        ('M226', 'Hinckley Sport Boats'),
        ('M227', 'Historic'),
        ('M228', 'Hobie'),
        ('M229', 'Holiday Mansion'),
        ('M230', 'Horizon'),
        ('M231', 'Houseboat'),
        ('M232', 'Hunt Yachts'),
        ('M233', 'Hunter'),
        ('M234', 'Hurricane'),
        ('M235', 'Hydra-Sports'),
        ('M236', 'Hylas'),
        ('M237', 'Idea'),
        ('M238', 'Iguana'),
        ('M239', 'Inmar'),
        ('M240', 'Interboat'),
        ('M241', 'Intrepid'),
        ('M242', 'Invincible'),
        ('M243', 'Iron'),
        ('M244', 'Island Gypsy'),
        ('M245', 'Island Packet'),
        ('M246', 'Itama'),
        ('M247', 'J Boats'),
        ('M248', 'JC'),
        ('M249', 'Jarrett Bay'),
        ('M250', 'Jarvis Newman'),
        ('M251', 'Javelin'),
        ('M252', 'Jeanneau'),
        ('M253', 'Jefferson'),
        ('M254', 'Jersey Cape'),
        ('M255', 'Johnson'),
        ('M256', 'Jongert'),
        ('M257', 'Jupiter'),
        ('M258', 'Karnic'),
        ('M259', 'Kawasaki'),
        ('M260', 'KenCraft'),
        ('M261', 'Kenner'),
        ('M262', 'Ketch'),
        ('M263', 'Key Largo'),
        ('M264', 'Key West'),
        ('M265', 'KingFisher'),
        ('M266', 'Kotter'),
        ('M267', 'Lagoon'),
        ('M268', 'Landau'),
        ('M269', 'Larson'),
        ('M270', 'Latitude 46'),
        ('M271', 'Lazzara'),
        ('M272', 'Legend'),
        ('M273', 'Leisure'),
        ('M274', 'Liberty'),
        ('M275', 'Lindell'),
        ('M276', 'Lion Yachts'),
        ('M277', 'Llaut'),
        ('M278', 'Lowe'),
        ('M279', 'Luhrs'),
        ('M280', 'Lund'),
        ('M281', 'MB'),
        ('M282', 'MJM'),
        ('M283', 'Mag Bay'),
        ('M284', 'Mainship'),
        ('M285', 'Majek'),
        ('M286', 'Majesty'),
        ('M287', 'Mako'),
        ('M288', 'Malibu'),
        ('M289', 'Manitou'),
        ('M290', 'Manta'),
        ('M291', 'Marex'),
        ('M292', 'Mariah'),
        ('M293', 'Maritime'),
        ('M294', 'Maritimo'),
        ('M295', 'Marlago'),
        ('M296', 'Marlin'),
        ('M297', 'Marlow'),
        ('M298', 'Marlow-Hunter'),
        ('M299', 'Marquis'),
        ('M300', 'Mason'),
        ('M301', 'Mastercraft'),
        ('M302', 'Maverick'),
        ('M303', 'Maxi'),
        ('M304', 'Maxum'),
        ('M305', 'May-Craft'),
        ('M306', 'McConaghy'),
        ('M307', 'McKee Craft'),
        ('M308', 'McKinna'),
        ('M309', 'Menorquin'),
        ('M310', 'Mercury Inflatables'),
        ('M311', 'Meridian'),
        ('M312', 'Midnight Express'),
        ('M313', 'Mikelson'),
        ('M314', 'Mirage'),
        ('M315', 'MirroCraft'),
        ('M316', 'Misty Harbor'),
        ('M317', 'Mochi Craft'),
        ('M318', 'Monark'),
        ('M319', 'Monte Carlo'),
        ('M320', 'Monte Carlo Yachts'),
        ('M321', 'Monte Fino'),
        ('M322', 'Montego Bay'),
        ('M323', 'Monterey'),
        ('M324', 'Moody'),
        ('M325', 'Moomba'),
        ('M326', 'Morris'),
        ('M327', 'Motor Yacht'),
        ('M328', 'Mulder'),
        ('M329', 'Myabca'),
        ('M330', 'Mystic'),
        ('M331', 'Mystic Powerboats'),
        ('M332', 'Najad'),
        ('M333', 'Narrowboat'),
        ('M334', 'NauticStar'),
        ('M335', 'Nautique'),
        ('M336', 'Nautitech'),
        ('M337', 'Nautor Swan'),
        ('M338', 'Naval Yachts'),
        ('M339', 'Nepallo'),
        ('M340', 'Neptunus'),
        ('M341', 'Nerea Yacht'),
        ('M342', 'Nimbus'),
        ('M343', 'Nitro'),
        ('M344', 'Nomad'),
        ('M345', 'Nor-Tech'),
        ('M346', 'Nord West'),
        ('M347', 'Nordhavn'),
        ('M348', 'Nordia'),
        ('M349', 'Nordic Tug'),
        ('M350', 'NorthCoast'),
        ('M351', 'Northmaster'),
        ('M352', 'Northstar'),
        ('M353', 'Nova'),
        ('M354', 'Novurania'),
        ('M355', 'Ocean Alexander'),
        ('M356', 'Ocean Explorer Catamarans'),
        ('M357', 'Ocean Express'),
        ('M358', 'Ocean Yachts'),
        ('M359', 'Ocqueteau'),
        ('M360', 'Offshore Yachts'),
        ('M361', 'One Design'),
        ('M362', 'Orkney'),
        ('M363', 'Osprey'),
        ('M364', 'Outback Yachts'),
        ('M365', 'Outer Reef Trident'),
        ('M366', 'Outer Reef Yachts'),
        ('M367', 'Outerlimits'),
        ('M368', 'Outremer'),
        ('M369', 'Oyster'),
        ('M370', 'Pachoud Yachts'),
        ('M371', 'Pacific Mariner'),
        ('M372', 'Pacific Seacraft'),
        ('M373', 'Paddle King'),
        ('M374', 'Palm Beach'),
        ('M375', 'Palm Beach Motor Yachts'),
        ('M376', 'Paragon'),
        ('M377', 'Pardo Yachts'),
        ('M378', 'Parker'),
        ('M379', 'Passport'),
        ('M380', 'Pathfinder'),
        ('M381', 'Pearl'),
        ('M382', 'Penn Yan'),
        ('M383', 'Performance'),
        ('M384', 'Pershing'),
        ('M385', 'Phoenix'),
        ('M386', 'Pioneer'),
        ('M387', 'Piranha'),
        ('M388', 'Playbuoy'),
        ('M389', 'Polar'),
        ('M390', 'Polar Kraft'),
        ('M391', 'Polaris'),
        ('M392', 'Pontoon'),
        ('M393', 'Premier'),
        ('M394', 'President'),
        ('M395', 'Prestige'),
        ('M396', 'Princecraft'),
        ('M397', 'Princess'),
        ('M398', 'Privateer'),
        ('M399', 'Privilege'),
        ('M400', 'Pro Sports'),
        ('M401', 'Pro-Line'),
        ('M402', 'ProCraft'),
        ('M403', 'ProKat'),
        ('M404', 'Protector'),
        ('M405', 'Pursuit'),
        ('M406', 'Queenship'),
        ('M407', 'Quicksilver'),
        ('M408', 'Qwest'),
        ('M409', 'RYCK'),
        ('M410', 'Rampage'),
        ('M411', 'Ranger'),
        ('M412', 'Ranger Tugs'),
        ('M413', 'Rapsody'),
        ('M414', 'Recon'),
        ('M415', 'Reflex'),
        ('M416', 'Regal'),
        ('M417', 'Regency'),
        ('M418', 'Regulator'),
        ('M419', 'Reinell'),
        ('M420', 'Release'),
        ('M421', 'Renegade'),
        ('M422', 'Rhea'),
        ('M423', 'Ribcraft'),
        ('M424', 'Ribeye'),
        ('M425', 'Rinker'),
        ('M426', 'Rio Yachts'),
        ('M427', 'Riva'),
        ('M428', 'Riviera'),
        ('M429', 'Robalo'),
        ('M430', 'Rodman'),
        ('M431', 'Rosborough'),
        ('M432', 'Rossiter'),
        ('M433', 'SACS'),
        ('M434', 'SPX RIB'),
        ('M435', 'Sabre'),
        ('M436', 'Sabreline'),
        ('M437', 'Saffier'),
        ('M438', 'Sailboat'),
        ('M439', 'Sailfish'),
        ('M440', 'Sanger'),
        ('M441', 'Sanlorenzo'),
        ('M442', 'Sanpan'),
        ('M443', 'Santa Cruz'),
        ('M444', 'Sargo'),
        ('M445', 'Sarnico'),
        ('M446', 'Savannah'),
        ('M447', 'Scarab'),
        ('M448', 'Schaefer'),
        ('M449', 'Schooner'),
        ('M450', 'Sciallino'),
        ('M451', 'Scout'),
        ('M452', 'Sea Born'),
        ('M453', 'Sea Cat'),
        ('M454', 'Sea Chaser'),
        ('M455', 'Sea Fox'),
        ('M456', 'Sea Hunt'),
        ('M457', 'Sea Pro'),
        ('M458', 'Sea Ray'),
        ('M459', 'Sea-Doo'),
        ('M460', 'Sea-Doo Sport Boats'),
        ('M461', 'SeaArk'),
        ('M462', 'SeaCraft'),
        ('M463', 'SeaHunter'),
        ('M464', 'Sealegs'),
        ('M465', 'Sealine'),
        ('M466', 'Sealver'),
        ('M467', 'Seaswirl'),
        ('M468', 'Seaswirl Striper'),
        ('M469', 'Seaward'),
        ('M470', 'Seawind'),
        ('M471', 'Selene'),
        ('M472', 'Sessa Marine'),
        ('M473', 'Shallow Sport'),
        ('M474', 'Shallow Stalker'),
        ('M475', 'Shamrock'),
        ('M476', 'ShearWater'),
        ('M477', 'Shoalwater'),
        ('M478', 'Silver Wave'),
        ('M479', 'Silverton'),
        ('M480', 'Sinergia'),
        ('M481', 'Skeeter'),
        ('M482', 'Skipjack'),
        ('M483', 'Sleepboot'),
        ('M484', 'Sloep'),
        ('M485', 'Sly'),
        ('M486', 'Smartliner'),
        ('M487', 'Smoker Craft'),
        ('M488', 'Solace'),
        ('M489', 'Solara'),
        ('M490', 'Solaris'),
        ('M491', 'Sonic'),
        ('M492', 'South Bay'),
        ('M493', 'SouthWind'),
        ('M494', 'Southfork'),
        ('M495', 'Southport'),
        ('M496', 'Sport-Craft'),
        ('M497', 'Sportsman'),
        ('M498', 'Spyder'),
        ('M499', 'Stamas'),
        ('M500', 'Starcraft'),
        ('M501', 'Starweld'),
        ('M502', 'Statement'),
        ('M503', 'Steiger Craft'),
        ('M504', 'Sterling'),
        ('M505', 'Stingray'),
        ('M506', 'Storebro'),
        ('M507', 'Stratos'),
        ('M508', 'Striper'),
        ('M509', 'Sumerset'),
        ('M510', 'Sun Tracker'),
        ('M511', 'SunCatcher'),
        ('M512', 'SunChaser'),
        ('M513', 'Sunbeam'),
        ('M514', 'Sundance'),
        ('M515', 'Sundeck Yachts'),
        ('M516', 'Sunreef'),
        ('M517', 'Sunsation'),
        ('M518', 'Sunseeker'),
        ('M519', 'Superyacht'),
        ('M520', 'Supreme'),
        ('M521', 'Sweetwater'),
        ('M522', 'Sylvan'),
        ('M523', 'Symbol'),
        ('M524', 'Tahoe'),
        ('M525', 'Tahoe Pontoon'),
        ('M526', 'Tartan'),
        ('M527', 'Tayana'),
        ('M528', 'Tender'),
        ('M529', 'Thunder Jet'),
        ('M530', 'Tiara Sport'),
        ('M531', 'Tiara Yachts'),
        ('M532', 'Tidewater'),
        ('M533', 'Tige'),
        ('M534', 'Tofinou'),
        ('M535', 'TomCat'),
        ('M536', 'Topaz'),
        ('M537', 'Tracker'),
        ('M538', 'Trailer'),
        ('M539', 'Trawler'),
        ('M540', 'Trifecta'),
        ('M541', 'Trimaran'),
        ('M542', 'Trintella'),
        ('M543', 'Triton'),
        ('M544', 'Triumph'),
        ('M545', 'Trojan'),
        ('M546', 'Trophy'),
        ('M547', 'True North'),
        ('M548', 'Trumpy'),
        ('M549', 'Trusty'),
        ('M550', 'Twin Vee'),
        ('M551', 'Uniesse'),
        ('M552', 'Valiant'),
        ('M553', 'VanDutch'),
        ('M554', 'Vanderbilt'),
        ('M555', 'Velocity'),
        ('M556', 'Venture'),
        ('M557', 'Veranda'),
        ('M558', 'Vexus'),
        ('M559', 'Viaggio'),
        ('M560', 'Vicem'),
        ('M561', 'Viking'),
        ('M562', 'Wajer'),
        ('M563', 'Walker Bay'),
        ('M564', 'War Eagle'),
        ('M565', 'Warrior'),
        ('M566', 'Wauquiez'),
        ('M567', 'WeldBilt'),
        ('M568', 'Weldcraft'),
        ('M569', 'Wellcraft'),
        ('M570', 'White Shark'),
        ('M571', 'Williams Jet Tenders'),
        ('M572', 'Windelo'),
        ('M573', 'Windy'),
        ('M574', 'World Cat'),
        ('M575', 'X Shore'),
        ('M576', 'X-Yachts'),
        ('M577', 'Xcursion'),
        ('M578', 'Xpress'),
        ('M579', 'Yamaha Boats'),
        ('M580', 'Yamaha WaveRunner'),
        ('M581', 'Yellowfin'),
        ('M582', 'Zeelander'),
        ('M583', 'Zeeschouw'),
        ('M584', 'Zodiac')
    ]

    listing_status = models.CharField(choices=LISTING_STATUS_CHOICES, max_length=1, verbose_name="Listing Status", default='A')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boat_listing')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    make = models.CharField(choices=BOAT_MODELS_LIST, max_length=5, verbose_name="Boat Make")
    model = models.CharField(max_length=25, verbose_name="Boat Model")
    price = models.PositiveIntegerField(verbose_name="Price", validators=[MinValueValidator(400)])
    tax_paid = models.CharField(choices=TAX_PAID_CHOICES, max_length=1, default='Y', verbose_name="Tax Status")
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=1, default='U', verbose_name="Condition")
    country = models.CharField(choices=COUNTRIES, max_length=2, default='UK', verbose_name="Country")
    location = models.CharField(max_length=50, default="", blank=True)
    year_construction = models.PositiveSmallIntegerField(verbose_name="Year of Construction", validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    length = models.DecimalField(decimal_places=2, max_digits=4, validators=[MinValueValidator(2.00), MaxValueValidator(50.00)], verbose_name="Length")
    beam = models.DecimalField(decimal_places=2, max_digits=4, validators=[MinValueValidator(2.00), MaxValueValidator(15.00)], verbose_name="Beam")
    draft = models.DecimalField(decimal_places=2, max_digits=4, validators=[MinValueValidator(0.10), MaxValueValidator(5.00)], verbose_name="Draft")
    weight = models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(500000)], verbose_name="Weight")
    type = models.CharField(choices=BOAT_TYPE, max_length=1, verbose_name="Type", default="P")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4, verbose_name="Category", default='PC')
    hull_material = models.CharField(choices=HULL_MATERIAL, max_length=1, verbose_name="Hull Material")
    hull_configuration = models.CharField(choices=HULL_CONFIG, max_length=1, verbose_name="Hull Configuration", default='M')
    fuel = models.CharField(choices=FUEL, max_length=1, verbose_name='Fuel Type')
    number_of_engines = models.PositiveSmallIntegerField(verbose_name="Number of main engines or motors", validators=[MinValueValidator(0), MaxValueValidator(9)], default=0)
    maximum_speed = models.PositiveSmallIntegerField(verbose_name="Maximum Speed", validators=[MinValueValidator(0),MaxValueValidator(99)])
    cruising_speed = models.PositiveSmallIntegerField(verbose_name="Cruising Speed", validators=[MinValueValidator(0),MaxValueValidator(99)])
    total_hp = models.PositiveSmallIntegerField(verbose_name="Total HP", validators=[MinValueValidator(0), MaxValueValidator(4000)], blank=True)
    cabins = models.PositiveSmallIntegerField(verbose_name="Cabins", validators=[MinValueValidator(0), MaxValueValidator(20)])
    berths = models.PositiveSmallIntegerField(verbose_name="Berths", validators=[MinValueValidator(0), MaxValueValidator(40)])
    heads = models.PositiveSmallIntegerField(verbose_name="Heads", validators=[MinValueValidator(0), MaxValueValidator(20)])
    listing_excerpt = models.CharField(max_length=66, verbose_name="Short Description")
    listing_description = models.TextField(max_length=5000, validators=[MaxLengthValidator(5000)])
    boat_feature_list = models.CharField(blank=True, max_length=3500, default='')
    featured_image = models.ImageField(verbose_name='Featured Image')
    featured_image_thumbnail = models.ImageField(verbose_name='Featured Image Thumnail', blank=True)

    def __str__(self):
        return f"{self.make} {self.model}"
    
    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"

    def get_absolute_url(self):
        return render(request, 'listings/index.html')

class ListingMedia(models.Model):
    listing = models.ForeignKey(Listings,on_delete=models.CASCADE, related_name='listing_media')
    image = models.FileField()

    def __str__(self):
        return f"{self.listing}"
